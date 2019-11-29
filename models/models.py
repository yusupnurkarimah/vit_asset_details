# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
import logging
_logger = logging.getLogger(__name__)
import datetime

class Asset(models.Model):
    _name = 'account.asset.asset'
    _inherit = ['account.asset.asset','mail.thread']

    pengadaan = fields.Selection(
    	selection=[
	    	('PO', 'PO'),
	    	('Pembelian Langsung', 'Pembelian Langsung')],
        string='Metode Pengadaan',
        required="true")
    sertifikat = fields.Selection(
    	selection=[
	    	('SHM', 'SHM'),
	    	('HGB', 'HGB')],
        string='Jenis Sertifikat')
    processor = fields.Char(
    	string='Processor',
    	size=50,
    	required=False)
    harddisk = fields.Char(
        string='Harddisk')
    memory = fields.Char(
        string='Memory')
    budget = fields.Char(
        string='Budget')
    kd_wilayah = fields.Char(
        string='Kode Wilayah')
    no_polisi = fields.Char(
        string='No. Polisi')
    tgl_pajak = fields.Date(
        string='Tanggal Pajak dan STNK',
        default=lambda *a : time.strftime("%Y-%m-%d"))
    tgl_asuransi = fields.Date(
        default=lambda *a : time.strftime("%Y-%m-%d"),
        string='Tanggal Asuransi')
    tanah = fields.Integer(
        string='Luas Tanah')
    bangunan = fields.Integer(
        string='Luas Bangunan')
    no_sertifikat = fields.Char(
        string='Nomor Sertifikat')
    tgl_sertifikat = fields.Date(
        default=lambda *a : time.strftime("%Y-%m-%d"),
        string='Tanggal Sertifikat')
    alamat = fields.Text(
        string='Alamat')
    tgl_jt_pajak = fields.Date(
        string='Tanggal Jatuh Tempo Pajak',
        default=lambda *a : time.strftime("%Y-%m-%d"))
    tgl_jt_asuransi = fields.Date(
        string='Tanggal Jatuh Tempo Asuransi',
        default=lambda *a : time.strftime("%Y-%m-%d"))
    
    def cek_jatuh_tempo(self):
        _logger.info('proses cek jatuh tempo.....')
        sql = "select id,name,tgl_jp_pajak from account_asset_asset where tgl_jp_pajak = %s"
        # date_jt = hari + 10 hari
        date_jt = datetime.datetime.now() + datetime.timedelta(days=10)

        cr = self.env.cr
        cr.execute(sql , (date_jt.strftime("%Y-%m-%d"),))
        res = cr.fetchall()


        def cek_jatuh_tempo(self):
        _logger.info('proses cek jatuh tempo.....')

        # date_jt = hari + 10 hari
        date_jt = datetime.datetime.now() + datetime.timedelta(days=10)
        assets = self.env['account.asset.asset'].search([('tgl_jp_pajak','=',date_jt)])
        for asset in assets:
            asset.message_post(body="Asset ini akan jatuh tempo 10 hari lagi",
                                message_type='comment',
                                subtype='mail.mt_comment')