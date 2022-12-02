# importamos la libreria de fastai con todas las funcionalidades
from fastai.vision.all import *
# importamos la libreria gradio
import gradio as gr

def is_cat(x):
	return x[0].isupper()
# cargamos nuestro modelo entrenado en fastai
learn = load_learner('model.pkl')
# definimos las categorias que nuestro modelo podra identificar
categories = ('Cat', 'Dog')
# Creamos una funcion para clasificar una imagen, en donde como parametro pasamos una imagen
def classify_image(img):
	pred, idx, probs = learn.predict(img)
	return dict(zip(categories, map(float, probs)))
# definimos el tamano de la imagen, 192 pixeles
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
# aqui definimos como se va a mostrar nuestra interfaz
intf = gr.Interface(fn=classify_image, inputs=image, outputs=label)
intf.launch(inline=False)
