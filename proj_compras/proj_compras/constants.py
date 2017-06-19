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

#CHoices para estado solicitud compra/ Cotizacion
APROBADO = 'A'
PENDIENTE = 'P'
RECHAZADO = 'R'

ESTADO_SOLICITUD_CHOICES = (
    (APROBADO, 'Aprobada'),
    (PENDIENTE, 'Pendiente'),
    (RECHAZADO, 'Rechazada'),
)
