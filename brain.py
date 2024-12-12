import os
import timeit
import numpy as np
import torch
import torch.nn as nn
import sklearn.metrics as skmetrics

from logger import get_logger

# Define the model architecture
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=64, kernel_size=50, stride=6, bias=False)
        self.bn1 = nn.BatchNorm1d(num_features=64, eps=0.001, momentum=0.01)
        self.relu1 = nn.ReLU(inplace=True)
        self.pool1 = nn.MaxPool1d(kernel_size=8, stride=8)
        self.drop1 = nn.Dropout(p=0.5)
        
        self.conv2 = nn.Conv1d(in_channels=64, out_channels=64, kernel_size=8, stride=1, bias=False)
        self.bn2 = nn.BatchNorm1d(num_features=64, eps=0.001, momentum=0.01)
        self.relu2 = nn.ReLU(inplace=True)
        self.pool2 = nn.MaxPool1d(kernel_size=4, stride=4)
        self.drop2 = nn.Dropout(p=0.5)
        
        self.fc = nn.Linear(in_features=384, out_features=5, bias=False)
    
    def forward(self, x):
        x = self.pool1(self.relu1(self.bn1(self.conv1(x))))
        x = self.drop1(x)
        x = self.pool2(self.relu2(self.bn2(self.conv2(x))))
        x = self.drop2(x)
        x = x.flatten(1)
        x = self.fc(x)
        return x

# Model class to handle training, evaluation, and saving/loading of checkpoints
class SimpleModel:
    def __init__(self, config, device):
        self.model = SimpleCNN()
        self.optimizer = torch.optim.Adam(self.model.parameters())
        self.loss_fn = nn.CrossEntropyLoss(reduce=False)
        self.device = device
        self.config = config
        self.model.to(self.device)
        self.global_epoch = 0
        self.global_step = 0

    def _compute_loss_and_metrics(self, x, y, w, sl):
        # Compute the model predictions
        y_pred = self.model(x)
        
        # Compute loss and apply weight (w)
        loss = self.loss_fn(y_pred, y)
        loss = torch.mul(loss, w)  # Weight padded samples
        loss = loss.sum() / w.sum()
        
        # Calculate accuracy and F1 score
        preds = np.reshape(np.argmax(y_pred.cpu().detach().numpy(), axis=1), (self.config["batch_size"], self.config["seq_length"]))
        trues = np.reshape(y.cpu().detach().numpy(), (self.config["batch_size"], self.config["seq_length"]))
        
        return loss, preds, trues

    def _process_minibatch(self, minibatch_fn):
        preds, trues, losses = [], [], []
        for x, y, w, sl, re in minibatch_fn:
            # Move data to device
            x, y, w = torch.from_numpy(x).to(self.device), torch.from_numpy(y).to(self.device), torch.from_numpy(w).to(self.device)
            
            # Compute loss and metrics for this batch
            loss, batch_preds, batch_trues = self._compute_loss_and_metrics(x, y, w, sl)
            
            # Accumulate loss and predictions
            losses.append(loss.cpu().detach().numpy())
            for i in range(self.config["batch_size"]):
                preds.extend(batch_preds[i, :sl[i]])
                trues.extend(batch_trues[i, :sl[i]])

        return preds, trues, losses

    def train(self, minibatch_fn):
        start = timeit.default_timer()
        self.model.train()
        self.optimizer.zero_grad()

        preds, trues, losses = self._process_minibatch(minibatch_fn)
        
        # Backpropagate and update parameters
        total_loss = np.array(losses).mean()
        total_loss.backward()
        self.optimizer.step()

        # Compute evaluation metrics
        accuracy = skmetrics.accuracy_score(trues, preds)
        f1 = skmetrics.f1_score(trues, preds, average="macro")
        confusion_matrix = skmetrics.confusion_matrix(trues, preds, labels=[0, 1, 2, 3, 4])

        # Log metrics and time taken
        stop = timeit.default_timer()
        duration = stop - start

        outputs = {
            "global_step": self.global_step,
            "train/trues": trues,
            "train/preds": preds,
            "train/accuracy": accuracy,
            "train/loss": total_loss,
            "train/f1_score": f1,
            "train/cm": confusion_matrix,
            "train/duration": duration
        }

        self.global_epoch += 1
        return outputs

    def evaluate(self, minibatch_fn):
        start = timeit.default_timer()
        self.model.eval()

        preds, trues, losses = self._process_minibatch(minibatch_fn)

        # Compute evaluation metrics
        total_loss = np.array(losses).mean()
        accuracy = skmetrics.accuracy_score(trues, preds)
        f1 = skmetrics.f1_score(trues, preds, average="macro")
        confusion_matrix = skmetrics.confusion_matrix(trues, preds, labels=[0, 1, 2, 3, 4])

        stop = timeit.default_timer()
        duration = stop - start

        outputs = {
            "test/trues": trues,
            "test/preds": preds,
            "test/accuracy": accuracy,
            "test/loss": total_loss,
            "test/f1_score": f1,
            "test/cm": confusion_matrix,
            "test/duration": duration
        }

        return outputs

    def save_checkpoint(self, name, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, f"{name}.ckpt")
        torch.save(self.model.state_dict(), save_path)
        return save_path

    def load_checkpoint(self, name, model_dir):
        load_path = os.path.join(model_dir, f"{name}.ckpt")
        self.model.load_state_dict(torch.load(load_path))
        return load_path


if __name__ == '__main__':
    model = SimpleCNN()
    fake_x = torch.randn(size=(2, 1, 3000))
    print(f"fake_x: {fake_x.shape}")
    y_pred = model(fake_x)
    print(f"y_pred: {y_pred.shape}")
    print('Successfully run the model')
