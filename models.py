from django.db import models
from django.contrib.auth.models import User

departments = [
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologists', 'Dermatologists'),
    ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
    ('Allergists/Immunologists', 'Allergists/Immunologists'),
    ('Anesthesiologists', 'Anesthesiologists'),
    ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
    ('Orthopaedi', 'Orthopaedi')
]

session_type = [
    ('Acute Pain Ward Round'),
    ('MDT'),
    ('Out Patient Clinic'),
    ('Pain Management'),
    ('Palliative Care'),
    ('Psychology'),
    ('Theatre Session'),
    ('Other Specialist Session')
]

sex = [
    ('Male', 'M'),
    ('Female', 'F')
]

consultation = [
    ('Domiciliary'),
    ('In Patient'),
    ('Intervention'),
    ('Out Patient Clinic - Dr only'),
    ('Out Patient Clinic - MDT'),
    ('Telephone'),
    ('E-mail'),
    ('Other')
]

contact_type = [
    ('New Assessment - Performed'),
    ('Follow Up Assessment - Performed'),
    ('New Procedure - Performed'),
    ('Repeat Procedure - Performed'),
    ('New Assessment - Observed'),
    ('Follow Up Assessment - Observed'),
    ('New Procedure - Observed'),
    ('Repeat Procedure - Observed')
]

supervision = [
    ('Solo'),
    ('Supervised - Direct'),
    ('Supervised - Indirect'),
    ('Teaching - Career Grade'),
    ('Teaching - Pain Trainee'),
    ('Teaching - Other')
]

pain_duration = [
    ('Less than 6 Months'),
    ('6 to 12 Months'),
    ('1 to 5 Years'),
    ('More than 5 Years')
]

pain_category = [
    ('Acute'),
    ('Cancer'),
    ('Chronic'),
    ('Other')
]

pain_type = [
    ('CRPS'),
    ('Neuropathic'),
    ('Nociceptive - Somatic'),
    ('Nociceptive - Visceral'),
    ('Mixed Neuropathic/Nociceptive'),
    ('Other')
]

pain_source = [
    ('Cardio-Respiratory'),
    ('Gastro-Intestinal'),
    ('Genito-Urinary'),
    ('Headache'),
    ('Metastatic'),
    ('Mixed Musculoskeletal & Neurological'),
    ('Musculoskeletal'),
    ('Neurological'),
    ('Phantom Limb'),
    ('Post Herpetic Neuralgia'),
    ('Post Surgical / Trauma'),
    ('Scar'),
    ('Trigeminal Neuralgia'),
    ('Vascular'),
    ('Affective'),
    ('Multiple Mechanisms'),
    ('Other')
]

pain_site = [
    ('Abdomen'),
    ('Chest'),
    ('Head / Face / Mouth'),
    ('Lumbar Region'),
    ('Lumbar & Lower Limb / Hip'),
    ('Lower Limb / Hip'),
    ('Neck'),
    ('Neck & Upper Limb / Shoulder'),
    ('Pelvic'),
    ('Thoracic Spine'),
    ('Upper Limb / Shoulder'),
    ('Uro-Genital'),
    ('Multiple Sites')
]

management_out_patient1 = [
    ('N/A'),
    ('Anticonvulsant'),
    ('Antidepressant'),
    ('Benzodiazepine'),
    ('NSAID'),
    ('Non Opioid Analgesic'),
    ('Weak Opioid Analgesic'),
    ('Strong Opioid Analgesic'),
    ('Topical Agents'),
    ('Systemic L.A.s'),
    ('TENS'),
    ('TSE'),
    ('List for Procedure'),
    ('Pain Management Programme'),
    ('Referral to Other Specialist'),
    ('Acupuncture'),
    ('Hypnosis'),
    ('Physiotherapy'),
    ('Psychology'),
    ('Relaxation'),
    ('Self Management'),
    ('Advice only'),
    ('Other')
]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=100, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=150, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=150, null=True)
    doctorName = models.CharField(max_length=150, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)


class medicine(models.Model):
    drugs_id = models.BigIntegerField(primary_key=True)
    drugs_code = models.CharField(max_length=100, null=True)
    drugs_type = models.CharField(max_length=20, null=True)
    drugs_name = models.CharField(max_length=200, null=True)
    expired_date = models.DateField(null=True)
    drugs_price = models.DecimalField(max_digits=10, decimal_places=2)
    drugs_composition = models.CharField(max_length=200, null=True)
    qty = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        managed = False
        db_table = 'hospital_medicine'

    # def __str__(self):
    #    return self.drugs_name
    # @property
    # def get_id(self):
    #    return self.id
    # property
    # def get_name(self):
    #    return self.drugs_name


class stock_barang(models.Model):
    kode_barang = models.CharField(max_length=100, null=True)
    bulan = models.CharField(max_length=10, null=True)
    tahun = models.CharField(max_length=4, null=True)
    no_sertifikat = models.CharField(max_length=50, null=True)
    no_pabrik = models.CharField(max_length=50, null=True)
    no_chasis = models.CharField(max_length=50, null=True)
    no_mesin = models.CharField(max_length=50, null=True)
    jenis_barang = models.CharField(max_length=20, null=True)
    type_barang = models.CharField(max_length=20, null=True)
    nama_barang = models.CharField(max_length=200, null=True)
    qty = models.IntegerField(null=True)
    harga_barang = models.DecimalField(max_digits=10, decimal_places=2)
    status_barang = models.CharField(max_length=100, null=True)
    ukuran_barang = models.CharField(max_length=100, null=True)
    bahan = models.CharField(max_length=100, null=True)
    tahun_perolehan = models.IntegerField(null=True)
    tanggal_buku = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)


class inventaris_barang(models.Model):
    id_awal = models.PositiveIntegerField(null=True)
    id_barang = models.PositiveIntegerField(null=True)
    kode_barang = models.CharField(max_length=100, null=True)
    bulan = models.CharField(max_length=10, null=True)
    tahun = models.CharField(max_length=4, null=True)
    reg = models.CharField(max_length=20, null=True)
    nama_barang = models.CharField(max_length=200, null=True)
    jns_barang = models.CharField(max_length=50, null=True)
    merk_barang = models.CharField(max_length=50, null=True)
    type_barang = models.CharField(max_length=50, null=True)
    no_sertifikat = models.CharField(max_length=50, null=True)
    no_pabrik = models.CharField(max_length=50, null=True)
    no_chasis = models.CharField(max_length=50, null=True)
    no_mesin = models.CharField(max_length=50, null=True)
    bahan = models.CharField(max_length=100, null=True)
    status_barang = models.CharField(max_length=20, null=True)
    cara_perolehan = models.CharField(max_length=20, null=True)
    tahun_perolehan = models.CharField(max_length=4, null=True)
    ukuran_barang = models.CharField(max_length=10, null=True)
    barang_B = models.CharField(max_length=5, null=True)
    barang_L = models.CharField(max_length=5, null=True)
    barang_R = models.CharField(max_length=5, null=True)
    barang_P = models.CharField(max_length=5, null=True)
    qty = models.IntegerField(null=True)
    harga_barang = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_buku = models.DateField(null=True)
    tahun_buku = models.CharField(max_length=4, null=True)
    keterangan = models.CharField(max_length=100, null=True)


class PatientDischargeDetails(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=150)
    assignedDoctorName = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)
    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)
    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)


class stock_poli(models.Model):
    kode_gol_barang = models.CharField(max_length=50, null=True)
    kode_jns_barang = models.CharField(max_length=50, null=True)
    kode_klp_barang = models.CharField(max_length=50, null=True)
    kode_barang = models.CharField(max_length=50, null=True)
    kode_pabrik = models.CharField(max_length=50, null=True)
    kode_barang_mix = models.CharField(max_length=100, null=True)
    nama_barang = models.CharField(max_length=100, null=True)
    nama_pabrik = models.CharField(max_length=100, null=True)
    penyedia = models.CharField(max_length=100, null=True)
    gudang = models.CharField(max_length=200, null=True)
    kode_penyedia = models.CharField(max_length=100, null=True)
    kode_gudang = models.CharField(max_length=100, null=True)
    status_aktif = models.BooleanField(null=True)
    nama_satuan_barang = models.CharField(max_length=100, null=True)
    status_aktf_pabrik = models.BooleanField(null=True)
    kel_barang = models.CharField(max_length=100, null=True)
    jns_barang = models.CharField(max_length=100, null=True)
    stock_awal = models.IntegerField(null=True)
    jumlah_masuk = models.IntegerField(null=True)
    jumlah_keluar = models.IntegerField(null=True)


class status_nyeri(models.Model):
    no_rkm_mds = models.CharField(max_length=100, null=False)
    nm_lngkp_pasien = models.CharField(max_length=50, null=True)
    tgl_lahir = models.CharField(max_length=10, null=True)
    bln_lahir = models.CharField(max_length=10, null=True)
    thn_lahir = models.CharField(max_length=4, null=True)
    tgl_datang = models.DateField(null=False)
    jam_datang = models.TimeField(null=False)
    ruang_perawatan = models.CharField(max_length=100, null=True)
    diagnosa_medis = models.CharField(max_length=100, null=True)
    riwayat_alergi = models.CharField(max_length=100, null=True)
    antikoagulasi = models.CharField(max_length=200, null=True)
    suhu = models.CharField(max_length=10, null=True)
    nadi = models.CharField(max_length=10, null=True)
    rr = models.CharField(max_length=10, null=True)
    td = models.CharField(max_length=10, null=True)
    tb = models.CharField(max_length=10, null=True)
    bb = models.CharField(max_length=10, null=True)
    kg = models.CharField(max_length=10, null=True)
    status_mental = models.CharField(max_length=10, null=True)
    riwayat_penyakit = models.CharField(max_length=50, null=True)
    pengobatan_saat_ini = models.CharField(max_length=50, null=True)
    status_nyeri = models.CharField(max_length=100, null=True)
    lokasi_nyeri = models.CharField(max_length=100, null=True)
    jenis_nyeri = models.CharField(max_length=100, null=True)
    intensitaas_nyeri = models.CharField(max_length=100, null=True)
    penyebab_nyeri = models.CharField(max_length=100, null=True)
    obat_anti_nyeri = models.CharField(max_length=100, null=True)
    arti_nyeri = models.CharField(max_length=100, null=True)
    pemeriksaan_lain = models.CharField(max_length=100, null=True)
    diagnosis = models.CharField(max_length=100, null=True)
    terapi = models.CharField(max_length=100, null=True)
    rencana_tindakan = models.CharField(max_length=100, null=True)
    dokter_consult_nyeri = models.CharField(max_length=100, null=True)


class consult_patient(models.Model):
    tanggal_consult = models.DateField(null=True)
    bulan = models.CharField(max_length=10, null=True)
    tahun = models.CharField(max_length=4, null=True)
    unit_kerja = models.CharField(max_length=50, null=True)
    instalasi = models.CharField(max_length=50, null=True)
    rekam_medis = models.CharField(max_length=50, null=True)
    nama_patient = models.CharField(max_length=100, null=True)
    tgl_lahir = models.DateField(null=True)
    usia = models.CharField(max_length=10, null=True)
    jns_kelamin = models.CharField(max_length=5, null=True)
    status_patient = models.CharField(max_length=5, null=True)
    alamat_patient = models.CharField(max_length=100, null=True)
    dpjp_consult = models.CharField(max_length=200, null=True)
    asal_departement = models.CharField(max_length=20, null=True)
    asal_ruangan = models.CharField(max_length=200, null=True)
    dpjp = models.CharField(max_length=200, null=True)
    riwayat_alergi = models.CharField(max_length=200, null=True)
    konsulan_to_dokter = models.CharField(max_length=200, null=True)
    diagnosa = models.CharField(max_length=200, null=True)
    pemberian_obat = models.CharField(max_length=200, null=True)
    tindakan = models.CharField(max_length=200, null=True)
    bhp_obat = models.CharField(max_length=100, null=True)
    rencana_tindak_lanjut = models.CharField(max_length=200, null=True)
    asal_bagian = models.CharField(max_length=200, null=True)
    keterangan = models.CharField(max_length=200, null=True)
    observasi_RR = models.CharField(max_length=200, null=True)
    pemberian_obat_RR = models.CharField(max_length=200, null=True)
    tindakan_RR = models.CharField(max_length=200, null=True)
    transfer_patient = models.CharField(max_length=100, null=True)


class prolotherapy_recoverygram(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    telp = models.CharField(max_length=15, null=True)
    diagnosis = models.CharField(max_length=200, null=True)
    date_of_onset = models.DateField(null=False)
    procedure = models.CharField(max_length=100, null=True)
    week_proress = models.CharField(max_length=10, null=True)
    activities_limited = models.CharField(max_length=10, null=True)
    rate_of_scale = models.CharField(max_length=10, null=True)
