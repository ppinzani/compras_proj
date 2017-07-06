# -*- coding: utf-8 -*-

#CHoices para condicion_iva
CONS_FINAL = 'CF'
RESPONSABLE_INSCRIPTO = 'RI'
RESPONSABLE_NO_INSCRIPTO = 'RNI'
MONOTRIBUTO = 'MONO'
NO_ESPECIFICA = 'NE'
OTRO = 'OTRO'

CONDICION_IVA_CHOICES = (
    (CONS_FINAL, 'Consumidor Final'),
    (NO_ESPECIFICA, 'No Especifica'),
    (RESPONSABLE_INSCRIPTO, 'IVA Responsable Inscripto'),
    (RESPONSABLE_NO_INSCRIPTO, 'IVA Responsable No Inscripto'),
    (MONOTRIBUTO, 'Monotributo'),
    (OTRO, 'Otro'),
)

#Choices para estado solicitud compra/ Cotizacion
SOLICITUD_APROBADA = 'A'
SOLICITUD_PENDIENTE = 'P'
ESTADO_SOLICITUD_CHOICES = (
    (SOLICITUD_APROBADA, 'Aprobada'),
    (SOLICITUD_PENDIENTE, 'Pendiente'),
)


#Choices para estado solicitud compra/ Cotizacion
COTIZACION_APROBADA = 'A'
COTIZACION_PENDIENTE = 'P'
COTIZACION_RECHAZADA = 'R'

ESTADO_COTIZACION_CHOICES = (
    (COTIZACION_APROBADA, 'Aprobada'),
    (COTIZACION_PENDIENTE, 'Pendiente'),
    (COTIZACION_RECHAZADA, 'Rechazada'),
)

#Choices para estado Pago
PAGO_PAGADO = 'Pa'
PAGO_PENDIENTE = 'Pe'

ESTADO_PAGO_CHOICES = (
    (PAGO_PAGADO, 'Pagado'),
    (PAGO_PENDIENTE, 'Pendiente'),
)


#Choices para Forma de Pago
CONTADO = 'E'
CUOTAS = 'C'

FORMA_DE_PAGO_CHOICES = (
    (CONTADO, 'Contado Efectivo'),
    (CUOTAS, 'En cuotas'),
)


#Choices para Tipo de Factura
FACTURA_A = "A"
FACTURA_B = "B"
FACTURA_C = "C"

TIPO_FACTURA_CHOICES = (
    (FACTURA_A, 'Factura A'),
    (FACTURA_B, 'Factura B'),
    (FACTURA_C, 'Factura C'),
)
