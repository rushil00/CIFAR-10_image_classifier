import unittest
import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from LeNet import *
import random

class TestModel(unittest.TestCase):

    def setUp(self):
        # Load the pre-trained model
        self.model = LeNet()
        self.model.load_state_dict(torch.load('./models/modelLenet.pth', map_location=torch.device('cpu')))
        self.model.eval()

        # Define transformations for the input image
        self.transform = transforms.Compose([
            transforms.ToTensor(),
        ])

        # Load CIFAR-10 test dataset
        self.test_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=self.transform)

    def test_prediction(self):
        # Define a DataLoader for the test dataset
        test_loader = DataLoader(self.test_dataset, batch_size=1, shuffle=True)

        # Get a random test image
        random_index = random.randint(0, len(self.test_dataset)-1)
        input_image, true_label = self.test_dataset[random_index]

        # Make prediction
        with torch.no_grad():
            output = self.model(input_image.unsqueeze(0))

        # Get the predicted class
        _, predicted_class = torch.max(output, 1)

        # Check if predicted class matches true class
        self.assertEqual(predicted_class.item(), true_label)

if __name__ == '__main__':
    unittest.main()