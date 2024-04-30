class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1,24,kernel_size=3,padding=1)
        self.act1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(24,12,kernel_size=3,padding=1)
        self.act2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2)
        self.fc1 = nn.Linear(12 * 12 * 12, 48)
        self.act3 = nn.ReLU()
        self.fc2 = nn.Linear(48, 5)

    def forward(self, x):
        out = self.pool1(self.act1(self.conv1(x)))
        out = self.pool2(self.act2(self.conv2(out)))
        out = out.view(-1, 12 * 12 * 12)
        out = self.act3(self.fc1(out))
        out = self.fc2(out)
        return out
