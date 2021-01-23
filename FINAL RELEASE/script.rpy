##FINAL

image lapbasket = "lapbasket.jpg"
image kamarkos = "kamarkos.jpg"
image char_boy = "boy.png"
image char_boy:
    "boy.png"
    xalign 0.75
    yalign 0.5
    zoom 1.5
image jalan = "jalan.jpg"
image kelas = "kelas.jpg"
image gazebo_mesin = "gazebo_mesin.jpg"
image gazjau = "gazjau.jpg"
image cafe = "cafe.jpg"
image cafe_lesehan = "cafe_lesehan.jpg"

image char_risa = "char_risa.png"
image char_risa:
    "char_risa.png"
    xalign 0.75
    yalign 0.38

define e = Character("Risa")
define i = Character("Boy", color="#f72d2d")

label start:
    play music "audio/bg_music.mp3" fadein 2.0 volume 0.4
    $ y = renpy.input("Siapa Nama Karakter Anda?")
    if y == "":
        "Isi Kembali Karakter Anda"
    y "Selamat Datang [y]"
    "Pilih alur cerita mana?"
    menu:
        "Risa":
            call jalan
            return
        "Boy":
            call lapbasket
            return
    label jalan:
    scene jalan
    "Cuaca hari ini sangatlah cerah, [y] melangkahkan kakinya menuju GKB 3 Universitas muhammadiyah malang untuk pertama kalinya. Hari ini adalah hari pertama ia kembali ke kampus setelah libur panjang."
    "Saat sampai di kelas, [y] segera memasuki ruangan itu dan duduk di sebelah Risa. "

    label kelas:
    scene kelas
    show char_risa with dissolve
    e "Hai [y], lama gak ketemu yaa, bagaimana liburanmu?"
    y "Menyenangkan. Aku banyak belajar hal baru, terutama tentang teknologi. Lalu, bagaimana denganmu?"
    e "Wah seru keknya, aku mengikuti beberapa internship untuk mengisi waktu luangku. "
    y "Banyak mencari pengalaman saat liburan ya?? "
    e "Iya nih. Btw, gimana kalau setelah pulang kuliah  kita belajar bareng sama temen-temen?"
    y "Hm, boleh juga nih. Biar nanti aku ajak temen-temen."
    e "Okey, eh dosennya udah masuk nih. Kita dengerin dosennya dulu."
    "Saat selesai kuliah hari itu, Risa menghampiri [y] untuk bertanya dimana mereka akan belajar bersama."
    e "Jadi belajar bareng?"
    y "Jadi dong, aku udah bilang ketemen-temen nih."
    e "enaknya belajar dimana ya??"
    menu :
        "Gazebo":
            y "gimana kalau kita belajar di Gazebo."
            call Gazebo
            return
        "Cafe":
            "gimana kalau kita belajar di cafe."
            call Cafe
            return

    label Gazebo:
    scene kelas
    show char_risa with dissolve
    e "boleh nih tapi, di kampus ini ada banyak gazebo.  Yang deket dari GKB 3 itu Gazebo Mesin dan yang jauh tuh, Gazebo perpustakaan. Kamu mau yang dimana?"
    menu :
        "Gazebo Dekat":
                "Gimana kalau yang deket aja jadi gak terlalu jauh dari gedung."
                e "yuk ke sana."
                call Gazdek
                return
        "Gazebo Jauh":
                "Gimana kalau gazebo yang jauh, kan dekat dengan perpustakaan. Siapa tau nanti kita butuh buku untuk materi yang kita pelajarin?"
                e "Boleh sih. Yaudah yuk kita kesana let's go!!"
                call GazJau
                return

    label Gazdek:
    scene gazebo_mesin
    show char_risa with dissolve
    "Akhirnya [y], [e], dan juga teman-temannya yang lain berjalan menuju Gazebo terdekat dari gedung."
    y "ngapain enaknya yah?"
    menu :
        "Istirahat":
            "Saat sampai gazebo, [y] memilih untuk duduk sambil bersandar pada pagar gazebo. "
            call gagal
            return
        "Nyimak Pembahasan Kelompok":
            "[y] mendengarkan dengan seksama penjelasan dari teman-temannya yang paham mengenai materi yang sedang mereka bahas."
            call berhasil
            return
        "Belajar":
            "Saat sampai gazebo [y] mengeluarkan bindernya dan beberapa buku yang ia punya tentang materi yang ia pelajari."
            call berhasil
            return

    label GazJau:
    scene gazjau
    show char_risa with dissolve
    "Akhirnya [y], [e], dan juga teman-temannya yang lain berjalan menuju Gazebo terjauh dari gedung."
    scene gazebo
    y "ngapain enaknya yah?"
    menu :
        "Istirahat":
            "Saat sampai gazebo, [y] memilih untuk duduk sambil bersandar pada pagar gazebo. "
            call gagal
            return
        "Nyimak Pembahasan Kelompok":
            "[y] mendengarkan dengan seksama penjelasan dari teman-temannya yang paham mengenai materi yang sedang mereka bahas."
            call berhasil
            return
        "Belajar":
            "Saat sampai gazebo [y] mengeluarkan bindernya dan beberapa buku yang ia punya tentang materi yang ia pelajari."
            call berhasil
            return

    label Cafe:
    scene Cafe
    show char_risa with dissolve
    e "boleh nih tapi, ada banyak cafe di seiktar kampus. Ada sih yang deket, di belakang kampus."
    y "yaudah gapapa di belakang kampus aja."
    "Mereka pun berjalan menuju belakang kampus, namun saat sampai sana, tempat duduknya ada yang lesehan dan juga di kursi."
    e "eh, duduk diman nih kita?"
    menu :
        "Duduk di kursi":
            y "Gimana kalau duduk di kursi jadi gak perlu lepas sepatu."
            e "yuk ke sana."
            call kursi
            return
        "Duduk Lesehan":
            y "Gimana kalau lesehn, jadi lebih santai belajarnya."
            e "Boleh sih. Yaudah yuk kita kesana let's go!!"
            call Lesehan
            return

    label kursi:
    scene cafe
    show char_risa with dissolve
    "Akhirnya [y], [e], dan juga teman-temannya yang lain berjalan menuju kursi yang sudah mereka pilih."
    y "ngapain enaknya yah?"
    menu :
        "Istirahat":
            "Saat sampai cafe, [y] memilih untuk duduk sambil bersandar pada kursi. "
            call gagal
            return
        "Nyimak Pembahasan Kelompok":
            "[y] mendengarkan dengan seksama penjelasan dari teman-temannya yang paham mengenai materi yang sedang mereka bahas."
            call berhasil
            return
        "Belajar":
            "Saat sampai cafe [y] mengeluarkan bindernya dan beberapa buku yang ia punya tentang materi yang ia pelajari."
            call berhasil
            return

    label Lesehan:
    scene cafe_lesehan
    show char_risa with dissolve
    menu:
        "Istirahat":
            "Saat sampai cafe, [y] memilih untuk duduk sambil bersandar pada dinding cafe. "
            call gagal
            return
        "Nyimak Pembahasan Kelompok":
            "[y] mendengarkan dengan seksama penjelasan dari teman-temannya yang paham mengenai materi yang sedang mereka bahas."
            call berhasil
            return
        "Belajar":
            "Saat sampai cafe [y] mengeluarkan bindernya dan beberapa buku yang ia punya tentang materi yang ia pelajari."
            call berhasil
            return

    label lapbasket:
    scene lapbasket
    "Pada Saat Sore Hari Selepas Mata Kuliah Struktur Data 3B aku Dan Boy Berencana Untuk Mampir Ke Kontrakan Boy Untuk Belajar Bersama Dikarenakan Besok Ada Ujian Struktur Data Bersama - Sama Agar Cepat Selesai."
    "Bagaimana Kuliah Hari Ini? Menyenangkan Bukan Besok Sudah Ujian Dan Gak Berasa Kita Kuliahnya Udah Sampai Ujung Semester 3"
    show char_boy with dissolve
    i "Yaa Lumayan , Namun Aku Masih Bingung Mau Belajar Dimana Soalnya Dikosku Rame Banyak Orang Sehingga Tidak Fokus Untuk Belajar"
    hide char_boy with dissolve
    "Kalau Begitu Ke Kontrakan Aja Kita Belajar Rame - Rame Agar Kita Besok Bisa Selesai Ujiannya"
    show char_boy with dissolve
    i "Yaudah Gass Skuy"
    hide char_boy with dissolve
    "Mereka pun Berangkat Ke Kontrakan Si Boy Untuk Belajar Bersama - Sama Akan Tetapi Ekspetasi Awal Yang Mau Belajar Bersama - Sama Untuk Ujian Besok Tidak Sesuai Dengan Realita Yang Mereka Alami Di Kontrakan."

    scene kamarkos
    "Akhirnya mereka sampai di kamar kos Boy"
    show char_boy with dissolve
    i "Akhirnya sampai juga"
    i "Capek banget ya kuliah hari ini"
    i "Mau mabar ga?"
    hide char_boy with dissolve
    menu:
        "Yuk deh gas!":
            call Mabar
            return
        "Ga ah aku mau numpang tidur bentar aja..":
            call Tidur
            return

    label Mabar:
    show char_boy with dissolve
    i "Oke sipp!"
    hide char_boy with dissolve
    "2 jam pun berlalu"
    show char_boy with dissolve
    i "Eh bukannya besok kita ada ujian yaa?"
    hide char_boy with dissolve
    menu:
        "Ga peduli ah kan masih ada temen hehe":
            call peduli
            return
        "Iya kah? waduh bentar aku tanya anak kelas dulu":
            call gapeduli
            return

    label Tidur:
        hide char_boy with dissolve
        "Yes akhirnya tidur, bentar aja deh yaa"
    menu:
        "Gas aja dah capek banget, ntar malem aja belajarnya":
            call tidurlama
            return
        "Bentar aja ah, belom siap buat ujian besok":
            call tidurBentar
            return

    label peduli:
        show char_boy with dissolve
        i "Cepet-cepet tanya ke anak kelas deh"
        i "Tanyain apa dia ada materi buat besok atau sekalian minta info jawaban pas besok aja dah haha"
        hide char_boy with dissolve
        menu:
            "Tanya materi ajadeh lagian juga gampang":
                call materi
                return
            "Besok aja kali ya sekalian infonya haha":
                call info
                return

    label gapeduli:
        show char_boy with dissolve
        i "Udah santai aja besok tuh gampang, bakal bisa ngerjain gapake belajar haha"
        hide char_boy with dissolve
        menu:
            "Gausa belajar karena yakin sudah bisa":
                call yakin
                return
            "Mencontek teman besok waktu tes":
                call contek
                return

    label tidurlama:
        "Ah bodo amat lagi capek juga, ntar malem bangunin aku ya"
        show char_boy with dissolve
        i "oke-oke"
        hide char_boy with dissolve
        "~~Kebangun pukul 7 malam"
        menu:
            "ah baru jam segini lanjut tidur aja deh":
                call lanjutTidur
                return
            "wah udah jam segini bangun dulu ah belajar":
                call belajarDulu
                return

    label tidurBentar:
        "bentar aja kali ya"
        "~~Kebangun pukul 7 malam"
        menu:
            "ah baru jam segini lanjut tidur aja deh":
                call lanjutTidur
                return
            "wah udah jam segini bangun dulu ah belajar":
                call belajarDulu
                return

    label materi:
        "Wahh ternyata materi besok banyak nih pelajari atau pasrah sebisanya aja yaa? haha"
        menu:
            "Paksa Pelajari":
                call berhasil
                return
            "Sebisanya aja deh":
                call gagal
                return

    label info:
        show char_boy with dissolve
        i "Ini enaknya tanya ke temen kita yang pinter apa yang se kontrakan aja?"
        hide char_boy with dissolve
        "Menurutku sih enaknya kita tanya ke..."
        menu:
            "Temen Kontrakan":
                call berhasil
                return
            "Temen yang pinter aja deh":
                call berhasil
                return

    label yakin:
        "Aduh itu kan materi yang baru kemaren dipelajarin gampang pasti"
        menu:
            "Kalo ada yang gabisa jawab sebisanya ajaa deh":
                call berhasil
                return
            "Kalo gabisa tinggal di asal aja jawabnya mah":
                call gagal
                return

    label contek:
        show char_boy with dissolve
        i "Hei kamu lupa ya kalo temen kelas kita tu banyak yang pinter tau jadi santai aja"
        "iya juga sih tapi nanti kita tanya dilaporin lagi haha, jadi enaknya nanya kesiapa ya?"
        hide char_boy with dissolve
        menu:
            "Teman-teman yang pinter":
                call gagal
                return
            "Teman-teman yang deket sama kita":
                call berhasil
                return

    label lanjutTidur:
        show char_boy with dissolve
        i "Udah lanjut aja nanti tengah malem kita paksa belajar"
        "Iya nih lagi capek banget, apa jawab sebisanya aja ya besok?"
        hide char_boy with dissolve
        menu:
            "Paksa belajar":
                call berhasil
                return
            "Jawab sebisanya aja besok":
                call gagal
                return

    label belajarDulu:
        show char_boy with dissolve
        i "Yuk deh belajar sekarang aja, tapi banyak nih materinya gimana?"
        hide char_boy with dissolve
        menu:
            "Belajar poin-poin nya aja":
                call berhasil
                return
            "Belajar semuanya dah gas":
                call berhasil
                return

    label berhasil:
        stop music fadeout 1.0
        "-GAME OVER-
        Selamat pilihanmu akan berdampak dengan berhasil lulus ujian besok :D"
        return
    label gagal:
        stop music fadeout 1.0
        "-GAME OVER-
        Yah pilihanmu bakal berdampak kamu gagal dalam ujian besok... ;("
        return
