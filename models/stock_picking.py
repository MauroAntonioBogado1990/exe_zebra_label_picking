# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_print_zebra_label(self):
        for picking in self:
            # ---------------------------------------------------------
            # CONFIGURACIÓN DE TAMAÑO DE ETIQUETA
            # Por defecto: 10x10 cm en impresora Zebra de 203 dpi
            # 1 cm ≈ 8 puntos → 10 cm = 800 puntos
            width = 800   # ancho en puntos
            length = 800  # alto en puntos

            # ---------------------------------------------------------
            # OPCIÓN ALTERNATIVA (DESCOMENTAR SI SE USA 300 dpi)
            # En 300 dpi ≈ 12 puntos por mm → 10 cm = 1200 puntos
            # width = 1200
            # length = 1200
            # ---------------------------------------------------------

            zpl = f"""
            ^XA
            ^PW{width}
            ^LL{length}
            ^CF0,40
            ^FO50,50^FDFecha: {fields.Date.today().strftime('%d-%m-%Y')}^FS
            ^FO50,100^FDDestinatario: {picking.partner_id.name} DNI {picking.partner_id.vat or ''}^FS
            ^FO50,150^FDDirección: {picking.partner_id.contact_address}^FS
            ^FO50,220^FDRemitente: {picking.company_id.name}^FS
            ^FO50,270^FDTel: {picking.company_id.phone or ''}^FS
            ^FO50,320^FDDirección: {picking.company_id.partner_id.contact_address}^FS
            ^FO50,390^FDProyecto: {picking.origin or 'N/A'}^FS
            ^FO50,440^FDBultos: 1 / 1^FS
            ^XZ
            """
            return {
                'type': 'ir.actions.report',
                'report_type': 'zebra_zpl',
                'data': {'zpl': zpl},
                'name': 'Etiqueta Zebra',
            }