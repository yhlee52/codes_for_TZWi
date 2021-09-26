import keras
import numpy as np
from keras import models
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics
from keras import regularizers
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

ReadData = np.loadtxt("eventcollect_STZct.csv", delimiter=",")

### train : validation : test = 6 : 2 : 2

num_of_data = len(ReadData)
print("Total number of data : ", num_of_data)
num_of_tr_val = (num_of_data // 5)*4
print("Number of test data : ", num_of_data - num_of_tr_val)

## Divide data and label
#origin_data = np.zeros((num_of_data, 41)) # For TT
origin_data = np.zeros((num_of_data, 25)) # For ST
origin_label = np.zeros(num_of_data)
origin_weight = np.zeros(num_of_data)

for i in range(0, num_of_data):
    origin_data[i] = ReadData[i][1:-1]
    origin_label[i] = ReadData[i][0]
    origin_weight[i] = ReadData[i][-1]

## Shuffle
idx = np.arange(origin_label.shape[0])
np.random.shuffle(idx)

origin_data = origin_data[idx]
origin_label = origin_label[idx]
origin_weight = origin_weight[idx]

## Data preparation
(train_data, train_label, train_weight), (test_data, test_label, test_weight) = (origin_data[:num_of_tr_val], origin_label[:num_of_tr_val], origin_weight[:num_of_tr_val]), (origin_data[num_of_tr_val:], origin_label[num_of_tr_val:], origin_weight[num_of_tr_val:])

#list_train_weight = train_weight.tolist()
train_data = np.array(train_data, dtype='float32')
test_data = np.asarray(test_data, dtype='float32')
train_label = np.asarray(train_label).astype('float32')
test_label = np.asarray(test_label).astype('float32')
train_weight = np.asarray(train_weight).astype('float32')
test_weight = np.asarray(test_weight).astype('float32')

## Data normalize
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

## Model
model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(train_data.shape[1],)))
#model.add(layers.Dropout(0.5))
#model.add(layers.BatchNormalization())
model.add(layers.Dense(64, activation='relu'))
#model.add(layers.Dropout(0.5))
#model.add(layers.BatchNormalization())
model.add(layers.Dense(64, activation='relu'))
#model.add(layers.Dropout(0.5))
#model.add(layers.BatchNormalization())
model.add(layers.Dense(32, activation='relu'))
#model.add(layers.Dropout(0.5))
#model.add(layers.BatchNormalization())
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

## Divide small set from train to monitor the model
realnum_train = len(train_data)
num_val = realnum_train // 4
print("Number of train data : ", realnum_train - num_val)
print("Number of val data : ", num_val)
val_data = train_data[:num_val]
partial_train_data = train_data[num_val:]
val_label = train_label[:num_val]
partial_train_label = train_label[num_val:]
val_weight = train_weight[:num_val]
partial_train_weight = train_weight[num_val:]

ptw_mean = partial_train_weight.mean(axis=0)
partial_train_weight -= ptw_mean
partial_train_weight += 1.
#ptw_std = partial_train_weight.std(axis=0)
#partial_train_weight /= ptw_std

history = model.fit(partial_train_data, partial_train_label, epochs=50, batch_size=512, validation_data=(val_data, val_label), sample_weight=partial_train_weight)

print("Training is Finished!")

## Draw ROC
test_pred = model.predict(test_data)
FPR, TPR, _ = roc_curve(test_label, test_pred)
plt.plot(FPR, TPR)
plt.plot([0,1],[0,1],'--', color='black') # 대각선
plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.savefig('ROC_curve_ST_Zct.png')
plt.clf()
aucscore = roc_auc_score(test_label, test_pred)
print("AUC score is : ", aucscore)
test_label_1 = test_label.reshape((num_of_data - num_of_tr_val, 1))
print(test_label_1)
test_pred_1 = np.where( test_pred < 0.5 , 0. , np.where( test_pred >= 0.5, 1. , test_pred))
print(test_pred_1)
cm = confusion_matrix(test_label_1, test_pred_1)
print("Confusion matrix : ", cm)
precision = precision_score(test_label_1, test_pred_1)
recall = recall_score(test_label_1, test_pred_1)
f1score = f1_score(test_label_1, test_pred_1)
print("Precision score : ", precision)
print("Recall score : ", recall)
print("f1 score : ", f1score)

## Plotting acc and loss
history_dict = history.history
history_dict.keys()

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc)+1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('ST_Zct_loss_622.png')

plt.clf()
acc = history_dict['acc']
val_acc = history_dict['val_acc']
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('ST_Zct_acc_622.png')

## Result
results = model.evaluate(test_data, test_label)
print(results)

model.save('ST_Zct.h5')

## Monitor output value
prediction = model.predict(test_data)
#part_prediction = prediction[:500]
#print(part_prediction)
plt.clf()
plt.hist(prediction, range=(0., 1.), bins=20)
plt.xlabel('Sigmoid output')
plt.ylabel('Events')
plt.savefig('ST_Zct_dist.png')