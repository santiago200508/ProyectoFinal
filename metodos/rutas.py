from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from modelos import modelos
from esquema import esquemas

router = APIRouter()


# ─── ROLES ───────────────────────────────────────────
@router.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    return db.query(modelos.Rol).all()


@router.get("/roles/{id_rol}")
def get_rol(id_rol: int, db: Session = Depends(get_db)):
    rol = db.query(modelos.Rol).filter(modelos.Rol.id_rol == id_rol).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.post("/roles")
def crear_rol(rol: esquemas.Rol, db: Session = Depends(get_db)):
    nuevo = modelos.Rol(nombre_rol=rol.nombre_rol)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/roles/{id_rol}")
def actualizar_rol(id_rol: int, rol: esquemas.Rol, db: Session = Depends(get_db)):
    item = db.query(modelos.Rol).filter(modelos.Rol.id_rol == id_rol).first()
    if not item:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    item.nombre_rol = rol.nombre_rol
    db.commit()
    db.refresh(item)
    return item


@router.delete("/roles/{id_rol}")
def borrar_rol(id_rol: int, db: Session = Depends(get_db)):
    item = db.query(modelos.Rol).filter(modelos.Rol.id_rol == id_rol).first()
    if not item:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    db.delete(item)
    db.commit()
    return f"Rol {id_rol} eliminado"


# ─── USUARIOS ────────────────────────────────────────
@router.get("/usuarios")
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(modelos.Usuario).all()


@router.get("/usuarios/{id_usuario}")
def get_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(modelos.Usuario).filter(
        modelos.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/usuarios")
def crear_usuario(usuario: esquemas.Usuario, db: Session = Depends(get_db)):
    nuevo = modelos.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        password=usuario.password,
        telefono=usuario.telefono,
        id_rol=usuario.id_rol
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/usuarios/{id_usuario}")
def actualizar_usuario(id_usuario: int, usuario: esquemas.Usuario, db: Session = Depends(get_db)):
    item = db.query(modelos.Usuario).filter(
        modelos.Usuario.id_usuario == id_usuario).first()
    if not item:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    item.nombre = usuario.nombre
    item.correo = usuario.correo
    item.password = usuario.password
    item.telefono = usuario.telefono
    item.id_rol = usuario.id_rol
    db.commit()
    db.refresh(item)
    return item


@router.delete("/usuarios/{id_usuario}")
def borrar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    item = db.query(modelos.Usuario).filter(
        modelos.Usuario.id_usuario == id_usuario).first()
    if not item:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(item)
    db.commit()
    return f"Usuario {id_usuario} eliminado"


# ─── CATEGORIAS ──────────────────────────────────────
@router.get("/categorias")
def get_categorias(db: Session = Depends(get_db)):
    return db.query(modelos.Categoria).all()


@router.get("/categorias/{id_categoria}")
def get_categoria(id_categoria: int, db: Session = Depends(get_db)):
    categoria = db.query(modelos.Categoria).filter(
        modelos.Categoria.id_categoria == id_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria


@router.post("/categorias")
def crear_categoria(categoria: esquemas.Categoria, db: Session = Depends(get_db)):
    nuevo = modelos.Categoria(
        nombre_categoria=categoria.nombre_categoria,
        descripcion=categoria.descripcion
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/categorias/{id_categoria}")
def actualizar_categoria(id_categoria: int, categoria: esquemas.Categoria, db: Session = Depends(get_db)):
    item = db.query(modelos.Categoria).filter(
        modelos.Categoria.id_categoria == id_categoria).first()
    if not item:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    item.nombre_categoria = categoria.nombre_categoria
    item.descripcion = categoria.descripcion
    db.commit()
    db.refresh(item)
    return item


@router.delete("/categorias/{id_categoria}")
def borrar_categoria(id_categoria: int, db: Session = Depends(get_db)):
    item = db.query(modelos.Categoria).filter(
        modelos.Categoria.id_categoria == id_categoria).first()
    if not item:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    db.delete(item)
    db.commit()
    return f"Categoria {id_categoria} eliminada"


# ─── PRODUCTOS ───────────────────────────────────────
@router.get("/productos")
def get_productos(db: Session = Depends(get_db)):
    return db.query(modelos.Producto).all()


@router.get("/productos/{id_producto}")
def get_producto(id_producto: int, db: Session = Depends(get_db)):
    producto = db.query(modelos.Producto).filter(
        modelos.Producto.id_producto == id_producto).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.post("/productos")
def crear_producto(producto: esquemas.Producto, db: Session = Depends(get_db)):
    nuevo = modelos.Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        stock=producto.stock,
        fecha_cosecha=producto.fecha_cosecha,
        fecha_vencimiento=producto.fecha_vencimiento,
        imagen=producto.imagen,
        id_categoria=producto.id_categoria
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/productos/{id_producto}")
def actualizar_producto(id_producto: int, producto: esquemas.Producto, db: Session = Depends(get_db)):
    item = db.query(modelos.Producto).filter(
        modelos.Producto.id_producto == id_producto).first()
    if not item:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    item.nombre = producto.nombre
    item.descripcion = producto.descripcion
    item.precio = producto.precio
    item.stock = producto.stock
    item.fecha_cosecha = producto.fecha_cosecha
    item.fecha_vencimiento = producto.fecha_vencimiento
    item.imagen = producto.imagen
    item.id_categoria = producto.id_categoria
    db.commit()
    db.refresh(item)
    return item


@router.delete("/productos/{id_producto}")
def borrar_producto(id_producto: int, db: Session = Depends(get_db)):
    item = db.query(modelos.Producto).filter(
        modelos.Producto.id_producto == id_producto).first()
    if not item:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(item)
    db.commit()
    return f"Producto {id_producto} eliminado"


# ─── PUNTOS DE ENTREGA ───────────────────────────────
@router.get("/puntos")
def get_puntos(db: Session = Depends(get_db)):
    return db.query(modelos.PuntoEntrega).all()


@router.get("/puntos/{id_punto}")
def get_punto(id_punto: int, db: Session = Depends(get_db)):
    punto = db.query(modelos.PuntoEntrega).filter(
        modelos.PuntoEntrega.id_punto == id_punto).first()
    if not punto:
        raise HTTPException(
            status_code=404, detail="Punto de entrega no encontrado")
    return punto


@router.post("/puntos")
def crear_punto(punto: esquemas.PuntoEntrega, db: Session = Depends(get_db)):
    nuevo = modelos.PuntoEntrega(
        nombre=punto.nombre,
        direccion=punto.direccion,
        ciudad=punto.ciudad
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/puntos/{id_punto}")
def actualizar_punto(id_punto: int, punto: esquemas.PuntoEntrega, db: Session = Depends(get_db)):
    item = db.query(modelos.PuntoEntrega).filter(
        modelos.PuntoEntrega.id_punto == id_punto).first()
    if not item:
        raise HTTPException(
            status_code=404, detail="Punto de entrega no encontrado")
    item.nombre = punto.nombre
    item.direccion = punto.direccion
    item.ciudad = punto.ciudad
    db.commit()
    db.refresh(item)
    return item


@router.delete("/puntos/{id_punto}")
def borrar_punto(id_punto: int, db: Session = Depends(get_db)):
    item = db.query(modelos.PuntoEntrega).filter(
        modelos.PuntoEntrega.id_punto == id_punto).first()
    if not item:
        raise HTTPException(
            status_code=404, detail="Punto de entrega no encontrado")
    db.delete(item)
    db.commit()
    return f"Punto {id_punto} eliminado"


# ─── PEDIDOS ─────────────────────────────────────────
@router.get("/pedidos")
def get_pedidos(db: Session = Depends(get_db)):
    return db.query(modelos.Pedido).all()


@router.get("/pedidos/{id_pedido}")
def get_pedido(id_pedido: int, db: Session = Depends(get_db)):
    pedido = db.query(modelos.Pedido).filter(
        modelos.Pedido.id_pedido == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.post("/pedidos")
def crear_pedido(pedido: esquemas.Pedido, db: Session = Depends(get_db)):
    nuevo = modelos.Pedido(
        id_usuario=pedido.id_usuario,
        estado=pedido.estado,
        total=pedido.total,
        id_punto_entrega=pedido.id_punto_entrega
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/pedidos/{id_pedido}")
def actualizar_pedido(id_pedido: int, pedido: esquemas.Pedido, db: Session = Depends(get_db)):
    item = db.query(modelos.Pedido).filter(
        modelos.Pedido.id_pedido == id_pedido).first()
    if not item:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    item.id_usuario = pedido.id_usuario
    item.estado = pedido.estado
    item.total = pedido.total
    item.id_punto_entrega = pedido.id_punto_entrega
    db.commit()
    db.refresh(item)
    return item


@router.delete("/pedidos/{id_pedido}")
def borrar_pedido(id_pedido: int, db: Session = Depends(get_db)):
    item = db.query(modelos.Pedido).filter(
        modelos.Pedido.id_pedido == id_pedido).first()
    if not item:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    db.delete(item)
    db.commit()
    return f"Pedido {id_pedido} eliminado"
