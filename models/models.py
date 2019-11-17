# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class Asset(models.Model):
    _name = 'account.asset.asset'
    _inherit = 'account.asset.asset'

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
        string='Jenis Sertifikat',
        required="true")
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