for layer in model.layers[:-3]:
    layer.trainable = False
model.summary()   
  
 #or we can use the follwing 
model.trainable=False # freezing the layer 
model.summary()
