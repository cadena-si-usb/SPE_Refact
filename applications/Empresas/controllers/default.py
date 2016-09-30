# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
#########################################################################


def index():

    response.flash = "Bienvenida Empresa"
    # return dict(message='Área de Empresas')
    return dict(form=login(), message="Empresas")

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow
    administrator to manage users
    """
    return dict(form=auth())

def login():
    formulario_login = SQLFORM.factory(
        Field('correo', label=T('Usuario o Correo Electronico'), required=True,
                requires=[IS_MATCH('^[a-zA-Z0-9.@_\\-]',error_message=T('Usuario o correo invalido.'))]),
        Field('clave', 'password',required=True,label=T('Contraseña')),
        captcha_field(),
        formstyle='bootstrap3_stacked'
       )

    if formulario_login.process(onvalidation=validar_credenciales).accepted:
        # Buscamos el usuario de web2py
        usuarioAuthSet = db(db.auth_user.email == request.vars.correo).select()
        usuarioBuscadoSet = None
        #
        if not usuarioAuthSet:
            # Si no lo encontramos entonces verificamos si es un usuario creado por
            # el catalogo de coordinador

            # Se busca si es una Empresa creada con el panel del coordinador
            # Primero buscamos en las empresas
            usuarioBuscadoSet = db(db.UsuarioExterno.correo == request.vars.correo).select()
            if usuarioBuscadoSet:
                usuarioBuscado = usuarioBuscadoSet[0]
                #Insertamos en la tabla User de Web2py, para el login
                auth.get_or_create_user({
                    "first_name":usuarioBuscado.nombre,
                    "clave":db.auth_user.clave.validate(usuarioBuscado.clave)[0],
                    "email":usuarioBuscado.correo})
                generar_Correo_Verificacion(usuarioBuscado.correo)
            else:
                response.flash = T("Usuario o Contraseña invalida.")
        # Si se encontro el usuario por cualquiera de los dos casos, proseguimos con el proceso de inicio de sesion
        if usuarioAuthSet or usuarioBuscadoSet:
            # Buscamos el id de la Empresa
            correoVerificarSet = db(db.correo_por_verificar.correo == request.vars.correo).select()
            if correoVerificarSet:
                redirect(URL(c='default', f='verifyEmail', vars=dict(correo=request.vars.correo)))
            else:
                tutor=db((db.UsuarioExterno.correo==request.vars.correo)
                         & (db.Tutor_Industrial.usuario==db.UsuarioExterno.id)).select()
                if (tutor.first() and tutor.first().Tutor_Industrial.comfirmado_Por_Empresa==0):
                    message = T(
                        'Usted Aun No Ha Sido Comfirmado Como Tutor Industrial Por Su Empresa, Por Lo Que Aun No Puede' \
                        'Iniciar Sesion')
                    redirect(URL(c='tutor_industrial', f='tutorNoComfirmado'))

                else:
                    auth.login_bare(request.vars.correo, request.vars.clave)
                    redirect(URL(c='default', f='home'))
                    response.flash = T("Inicio Exitoso")
    return formulario_login

def resendVerificationEmail():

    correoVerificarSet = db(db.correo_por_verificar.correo == request.vars.correo).select()

    reenviar_Correo_Verificacion(request.vars.correo)

    redirect(URL(c='default',f='verifyEmail',
        vars=dict(correo=request.vars.correo,resend= T("El Correo ha sido reenviado"),
        message=T("Verificacion de Correo"))))

def verifyEmail():
    form = SQLFORM.factory(Field('codigo', label=T('Codigo De Verificacion'), required=True,requires=IS_NOT_EMPTY(error_message=T('Este campo es necesario'))),formstyle='bootstrap3_stacked'
                           )

    form.add_button(T('Send Email Again'), URL(c='default',f='resendVerificationEmail'
        ,vars=dict(correo=request.vars.correo)))

    usuarioSet = db(db.UsuarioExterno.correo == request.vars.correo).select()
    usuario = usuarioSet[0]
    contrasena = usuario.clave

    if form.process().accepted:
        # Buscamos el id de la Empresa
        correoVerificarSet = db(db.correo_por_verificar.correo == request.vars.correo).select()
        if correoVerificarSet[0].codigo != request.vars.codigo:
            response.flash = T("Codigo incorrecto")
        else:
            db(db.correo_por_verificar.correo == request.vars.correo).delete()
            # Verificamos si es un tutor industrial y si ya fue comfirmado
            tutor = db((db.UsuarioExterno.correo == request.vars.correo)
                       & (db.Tutor_Industrial.usuario == db.UsuarioExterno.id)).select()
            if (tutor.first() and tutor.first().Tutor_Industrial.comfirmado_Por_Empresa == 0):
                message = T(
                    'Usted Aun No Ha Sido Comfirmado Como Tutor Industrial Por Su Empresa, Por Lo Que Aun No Puede' \
                    'Iniciar Sesion')
                redirect(URL(c='tutor_industrial', f='tutorNoComfirmado'))
            else:
                auth.login_bare(request.vars.correo,contrasena)
                redirect(URL(c='default',f='home'))
    return response.render('default/codigoVerificacion.html',
        message=T("Verificacion de Correo"),resend= request.vars.resend,
        form=form,vars=dict(correo=request.vars.correo))


def validar_credenciales(form):
    # Buscamos al usuario
    login_Usuario  = db(db.UsuarioExterno.correo  == form.vars.correo)

    #Solo puedo encontrar alguno de los dos, verifico el clave
    if not login_Usuario.isempty():
        datosUsuario = login_Usuario.select()[0]
        if datosUsuario.clave != form.vars.clave:
            form.errors = "Usuario o contraseña invalida"

def logout():
    url = (URL(c='default',f='index'))
    auth.logout(next=url)

@auth.requires(auth.is_logged_in())
def home():
    return response.render('default/home.html')

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
