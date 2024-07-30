import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from weasyprint import HTML
from .models import Genero, Director, Pais, Pelicula, Cine
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request, 'home.html')
#Renderizndon el template de listado Genero
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request, "listadoGeneros.html", {'generos':generosBdd})
#Se recibe el id para eliminar un genero 
def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Genero Eliminado Exitosamente.")
    return redirect('listadoGeneros')
#Renderizando formiulario de nuevo genero 
def nuevoGenero(request):
    return render(request, "nuevoGenero.html")
#Insertando generos en la bdd
def guardarGenero(request):
    nom=request.POST['nombre']
    des=request.POST['descripcion']
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=des,foto=fot)
    messages.success(request,"Genero registrado exitosamente.")
    return redirect('listadoGeneros')
#Renderizando formulario de actualizacion 
def editarGenero(request, id):
    generoEditar=Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'genero':generoEditar})
#actualizando los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request, "Genero actualizado exitosamente.")
    return redirect('listadoGeneros')

# Renderizando el template de listado Director
def listadoDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directoresBdd})

# Se recibe el id para eliminar un director
def eliminarDirector(request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

# Renderizando formulario de nuevo director
def nuevoDirector(request):
    return render(request, "nuevoDirector.html")

# Insertando directores en la bdd
def guardarDirector(request):
    nom = request.POST['nombre']
    des = request.POST['descripcion']
    fot = request.FILES.get("foto")
    nuevoDirector = Director.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, "Director registrado exitosamente.")
    return redirect('listadoDirectores.html')

# Renderizando formulario de actualización
def editarDirector(request, id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'director': directorEditar})

# Actualizando los nuevos datos en la BDD
def procesarActualizacionDirector(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    directorConsultado = Director.objects.get(id=id)
    directorConsultado.nombre = nombre
    directorConsultado.descripcion = descripcion
    directorConsultado.save()
    messages.success(request, "Director actualizado exitosamente.")
    return redirect('listadoDirectores.html')

#Renderizndon el template de listado Paises
def listadoPais(request):
    paisesBdd=Pais.objects.all()
    return render(request, "listadoPais.html", {'paises':paisesBdd})
#Renderizndon el template de listado Peliculas
def listadoPeliculas(request):
    peliculaBdd=Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas':peliculaBdd})

#Funcion para gestionar el crud del cine
def gestionCines(request):
    return render(request,'gestionCines.html')
#Insertando cines mediante AJAX en la Base de Datos
@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.',
        
    })

#Renderizando el listado de cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html",
                  {'cines':cines})

#funcion para gestionar el CRUD de Director
def gestionDirectores(request):
    return render(request, 'gestionDirectores.html')

def gestionPeliculas(request):
    return render(request, 'gestionPeliculas.html')

@csrf_exempt
def insertar_director(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dni = data['dni']
        apellido = data['apellido']
        nombre = data['nombre']
        estado = data.get('estado', False)
        director = Director(dni=dni, apellido=apellido, nombre=nombre, estado=estado)
        director.save()

        return JsonResponse({'message': 'Director insertado correctamente'}, status=200)

    return JsonResponse({'message': 'Error al insertar el director'}, status=400)

# Función para eliminar una película por su ID
def eliminar_pelicula(request, id):
    try:
        # Obtener la película por su ID
        pelicula = Pelicula.objects.get(id=id)
        # Eliminar la película
        pelicula.delete()
        # Devolver un mensaje de éxito como JSON
        return JsonResponse({'message': f'La película "{pelicula.titulo}" ha sido eliminada correctamente.'})
    except Pelicula.DoesNotExist:
        # Si la película no existe, devolver un mensaje de error
        return JsonResponse({'message': 'La película no existe.'}, status=404)
    except Exception as e:
        # Manejar otros errores y devolver un mensaje de error genérico
        return JsonResponse({'message': str(e)}, status=500)

#funcion para gestionar el CRUD de Pelicula
@csrf_exempt
def insertar_pelicula(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        titulo = data['titulo']
        duracion = data['duracion']
        sinopsis = data['sinopsis']
        genero_id = data['genero_id']
        director_id = data['director_id']
        genero = Genero.objects.get(nombre=genero_id)
        director = Director.objects.get(nombre=director_id)
        pelicula = Pelicula(titulo=titulo, duracion=duracion, sinopsis=sinopsis, genero_id=genero_id, director_id=director_id)
        pelicula.save()

        return JsonResponse({'message': 'Película insertada correctamente'}, status=200)

    return JsonResponse({'message': 'Error al insertar la película'}, status=400)

def consultar_directores(request):
    if request.method == 'GET':
        directores = list(Director.objects.values())
        return JsonResponse(directores, safe=False)

def consultar_peliculas(request):
    if request.method == 'GET':
        peliculas = list(Pelicula.objects.values())
        return JsonResponse(peliculas, safe=False)
    
def exportCines(request):
    dataCines = Cine.objects.all()
    return render(request,"exportCines.html", {'cines':dataCines})

def exportCinesPDF(request):
    #llamar a todos los datos del modelo cina
    cines = Cine.objects.all()
    #llamar al template con el render string
    html_string = render_to_string('exportCines.html', {'cines': cines}) # type: ignore
    #almacenar como un archivo html
    html = HTML(string=html_string)
    #leer todo el html guardado y convvertirlo en un pdf
    pdf = html.write_pdf()
    #dar una respuesta como pdf(archivo)
    response = HttpResponse(pdf, content_type='application/pdf')
    #nombrar y dar una extension al archivo expotado
    response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
    #exportar archivo
    return response