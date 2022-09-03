import collections

import seaborn as sns
import xgboost
from sklearn.model_selection import train_test_split


from src.DataProvider import DataProvider
from src.DataUtils import *
import matplotlib.pyplot as plt

ARCHIVE_DIR = "archive"


def plot_2_first_imgs(images, dim=8):
    image = images[0]
    plt.imshow(image)
    plt.show()
    image = images[1]
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    dp = DataProvider(None)
    images, labels = skin_cancer_detector_parse_dataset_28_28_RGB(ARCHIVE_DIR)
    X, y = images, labels
    X_train_and_val, X_test, y_train_and_val, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # NOTE: Don't forget to not use test data.

    X_train, X_val, y_train, y_val = train_test_split(X_train_and_val, y_train_and_val, test_size=0.2, random_state=0)

    X_dev, y_dev = X_train[:100], y_train[:100]   # Development dataset (only used for quick testing).

    # Visualize some examples from the dataset.
    # We show a few examples of training images from each class.  # TODO-Sahar: Will recheck that I didn't mess this up:
    classes = ['akiec', 'bcc', 'bkl', 'df', 'nv', 'vasc', 'mel']
    num_classes = len(classes)
    samples_per_class = 7
    for y, cls in enumerate(classes):
        idxs = np.flatnonzero(y_train == y)
        idxs = np.random.choice(idxs, samples_per_class, replace=False)
        for i, idx in enumerate(idxs):
            plt_idx = i * num_classes + y + 1
            plt.subplot(samples_per_class, num_classes, plt_idx)
            plt.imshow(X_train[idx].astype('uint8'))
            plt.axis('off')
            if i == 0:
                plt.title(cls)
    plt.show()

    classes_map = {i: name for i, name in enumerate(classes)}
    labels_as_names = list(map(lambda k: classes_map[k], y_train))
    ax = sns.displot(labels_as_names)
    plt.show()

    colors = sns.color_palette('pastel')[0:len(labels)]
    counter = collections.Counter(y_train)
    percentage_per_class = [counter[i] for i in range(num_classes)]
    plt.pie(percentage_per_class, labels=classes, colors=colors, autopct='%.0f%%')
    plt.show()

    print("Start training...")
    model = xgboost.XGBClassifier()
    model.fit(X_train.reshape((len(y_train), -1)), y_train)
    val_predictions = model.predict(X_val.reshape((len(y_val), -1)))
    accuracy = np.mean(val_predictions == y_val, axis=0)
    print(f"Accuracy: {accuracy}")



# Sahar's Notes:
# Counter(labels)
# Out[23]: Counter({2: 1099, 4: 6705, 3: 115, 6: 1113, 5: 142, 1: 514, 0: 327})
# Counter(metadata_df["dx"])
# Out[24]:
# Counter({'bkl': 1099,
#          'nv': 6705,
#          'df': 115,
#          'mel': 1113,
#          'vasc': 142,
#          'bcc': 514,
#          'akiec': 327})