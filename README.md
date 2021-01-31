# Bulanik-Mantik-ile-Yazilim-Risk-Yonetimi

Yapay Zekânın bir alt dalı ve çalışma alanı olan Bulanık Mantık bilgisayarın çalışma prensibi olan “0” ve “1” lerden oluşan ikili mantık yerine çok daha kapsamlı bir cevap olanağı sunan sisteme denilmektedir. Kısaca bulanık mantık, klasik mantığa göre net cevaplar yerine olabilitesi olan her türlü koşulu değerlendiren sisteme denilmektedir.  

Yazılım Risk Yönetimi ise bir proje geliştirirken ortaya çıkabilecek olumsuzlukların önceden hesaplanarak hem maliyetin  hem de diğer etkenlerin korunmasını sağlamaktadır. Böylelikle bir projeye başlamadan önce Yazılım Risk Yönetimi sayesinde olumsuzluklar minimuma indirilerek mantıklı adımlarla projeye başlanır. Bu sayede, geliştirme sürecinde yüksek maliyetlerden korunup en doğru şekilde yazılım yaşam döngüleri takip edilir ve verimli bir çalışma gerçekleştirilir. 

Yapılan bu projede, “Yazılım Risk Yönetimi”, “Bulanık Mantık” yapısı ile birleştirilerek, bir yazılım geliştirme çalışmasının durumunun (öngörülen ve belirtilen sisteme girdi olarak verilen değişkenlerin) takip edilebildiği bir risk tespiti sistemi oluşturulmuştur. Sistem oluşturulurken bir projenin gerçekleşmesine katkı sağlayan ve risk teşkil eden değişkenler kararlaştırılıp sistemden çıktı olarak projenin gerçekleşmesindeki risk hesaplanması yapılmaktadır. 
Anahtar Kelimeler : Yazılım Risk Yönetimi, Bulanıklaştırma, Durulama, Bulanık Mantık



<h> YAZILIM RISK YÖNETIMININ UYGULAMA YÖNTEMI <h/>

Bu projemizi gerçekleştirmedeki amacımız uluslararası ya da yerli olarak yapılan bir yazılım projesini başarıya taşıyan ve risk teşkil eden değişkenlerin, bulanık mantık yöntemi ile belirlenip kullanıcıya bilgi vermesidir.

Sistemimiz 9 girişten ve 1 çıkıştan ulaşmaktadır.  Giriş olarak;

Proje Hakimiyeti, Proje Deneyimi (Proje için kullanılacak sistemleri daha önce deneyimlemiş olmak), İletişim (Ekipte yer alan kişilerin kendi aralarında kurdukları projenin ilerlemesi için gerçekleştirdiği bilgi ve kaynak alışverişi), Adım Adım İlerleme (Yazılım süreç yöntemlerinin sırasıyla güncel yazılım metotlarının uygulanarak ilerlenmesi), Kaynak Çeşitliliği (Proje için kullanılacak sistemleri açıklayan kaynakların yeterliliği), Ekip Deneyimi (Proje gerçekleştirecek kişilerinin daha önce başka projelerde beraber çalışıp çalışmama durumu), Gerekliliklerin Sabit Kalması (Projeyi gerçekleştireceğimiz kişilerinin taleplerinin en başından ), Gereklilikler Birbirine Bağlılığı (Bir sorun ile karşılaşıldığında iç sistemdeki diğer bölümleri etkileme olasılığı ve son olarak Zaman Dilimi (Uluslararası bir projede yer alan ekip üyelerinin farklı zaman dilimlerine göre yaşaması) değişkenleri kullanılmaktadır.

Bulanık kümelerin oluşturulması için belirlediğimiz giriş ve çıkış değerleri için, dilsel değerleri belirten bulanık kümeleri aşağıdaki gibi oluşturduk:

• Gerekliliklerin sabit kalması: Düşük, Orta, Yüksek
• Görevlerin birbirine bağlılığı: Düşük, Orta, Yüksek
• Kaynak Çeşitliliği: Çok düşük, Düşük, Orta, Yüksek, çok yüksek
• Adım adım ilerleme: Düşük, Orta, Yüksek
• Zaman Dilimi Farklılığı: Düşük, Orta, Yüksek
• Proje süreci Hakimiyeti: Düşük, Orta, Yüksek
• Ekip deneyimi: Çok düşük, Düşük, Orta, Yüksek, çok yüksek
• Proje deneyimi: Çok düşük, Düşük, Orta, Yüksek, çok yüksek
• İletişim: Düşük, Orta, Yüksek
• Risk: Çok düşük, Düşük, Orta, Yüksek, çok yüksek

     Üyelik fonksiyonlarının oluşturulması Belirtilen bulanık kümeler için üçgen üyelik fonksiyonları kullanarak, simetrik olarak, aşağıdaki grafikleri oluşturduk. 

