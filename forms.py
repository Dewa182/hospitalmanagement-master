from django import forms
from django.contrib.auth.models import User
from . import models

# for admin signup


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

# for student related form


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address', 'mobile', 'department', 'status', 'profile_pic']


class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.medicine
        fields = ['drugs_id', 'drugs_code', 'drugs_type', 'drugs_name',
                  'expired_date', 'drugs_price', 'drugs_composition', 'qty', 'description']


class Stock_PoliForm(forms.ModelForm):
    class Meta:
        model = models.stock_poli
        fields = ['kode_gol_barang', 'kode_gol_barang', 'kode_jns_barang', 'kode_klp_barang', 'kode_barang', 'kode_pabrik', 'kode_barang_mix', 'nama_barang', 'nama_pabrik', 'penyedia',
                  'gudang', 'kode_penyedia', 'kode_gudang', 'status_aktif', 'nama_satuan_barang', 'status_aktf_pabrik', 'kel_barang', 'jns_barang', 'stock_awal', 'jumlah_masuk', 'jumlah_keluar']


class Stock_BarangForm(forms.ModelForm):
    class Meta:
        model = models.stock_barang
        fields = ['kode_barang', 'bulan', 'tahun', 'no_sertifikat', 'no_pabrik', 'no_chasis', 'no_mesin', 'jenis_barang', 'type_barang',
                  'nama_barang', 'qty', 'harga_barang', 'status_barang', 'ukuran_barang', 'bahan', 'tahun_perolehan', 'tanggal_buku', 'description']


class Inventaris_BarangForm(forms.ModelForm):
    class Meta:
        model = models.inventaris_barang
        fields = ['id_awal', 'id_barang', 'kode_barang', 'bulan', 'tahun', 'reg', 'nama_barang', 'jns_barang', 'merk_barang', 'type_barang', 'no_sertifikat', 'no_pabrik', 'no_chasis', 'no_mesin', 'bahan',
                  'status_barang', 'cara_perolehan', 'tahun_perolehan', 'ukuran_barang', 'barang_B', 'barang_L', 'barang_R', 'barang_P', 'qty', 'harga_barang', 'tanggal_buku', 'tahun_buku', 'keterangan']


class Status_NyeriForm(forms.ModelForm):
    class Meta:
        model = models.status_nyeri
        fields = ['no_rkm_mds', 'nm_lngkp_pasien', 'tgl_lahir', 'bln_lahir', 'thn_lahir', 'tgl_datang', 'jam_datang', 'ruang_perawatan', 'diagnosa_medis', 'riwayat_alergi', 'antikoagulasi', 'suhu', 'nadi', 'rr', 'td', 'tb', 'bb', 'kg', 'status_mental',
                  'riwayat_penyakit', 'pengobatan_saat_ini', 'status_nyeri', 'lokasi_nyeri', 'jenis_nyeri', 'intensitaas_nyeri', 'penyebab_nyeri', 'obat_anti_nyeri', 'arti_nyeri', 'pemeriksaan_lain', 'diagnosis', 'terapi', 'rencana_tindakan', 'dokter_consult_nyeri']


class Consult_PatientForm(forms.ModelForm):
    class Meta:
        model = models.consult_patient
        fields = ['tanggal_consult', 'rekam_medis', 'nama_patient', 'tgl_lahir', 'usia', 'jns_kelamin', 'status_patient', 'alamat_patient', 'dpjp_consult', 'asal_departement', 'asal_ruangan', ''
                  'dpjp', 'riwayat_alergi', 'konsulan_to_dokter', 'diagnosa', 'pemberian_obat', 'tindakan', 'bhp_obat', 'rencana_tindak_lanjut', 'asal_bagian', 'keterangan', 'observasi_RR', 'pemberian_obat_RR', 'tindakan_RR', 'transfer_patient']


class prolotherapy_recoverygramForm(forms.ModelForm):
    class Meta:
        model = models.prolotherapy_recoverygram
        fields = ['name', 'address', 'telp', 'diagnosis', 'date_of_onset',
                  'procedure', 'week_proress', 'activities_limited', 'rate_of_scale']

# for teacher related form


class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
    # this is the extrafield for linking patient and their assigend doctor
    # this will show dropdown __str__ method doctor model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all(
    ).filter(status=True), empty_label="Name and Department", to_field_name="user_id")

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']


class AppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(
        status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(
        status=True), empty_label="Patient Name and Symptoms", to_field_name="user_id")

    class Meta:
        model = models.Appointment
        fields = ['description', 'status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(
        status=True), empty_label="Doctor Name and Department", to_field_name="user_id")

    class Meta:
        model = models.Appointment
        fields = ['description', 'status']

# for contact us page


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# class ContactusForm(forms.Form):
#        captcha = CaptchaField()

# class Meta:
#        model = User
#        fields = ("username", "email", "password1", "password2")

# def save(self, commit=True):
#        user = super(NewUserForm, self).save(commit=False)
#        user.email = self.cleaned_data['email']
#        if commit:
#            user.save()
#        return user
