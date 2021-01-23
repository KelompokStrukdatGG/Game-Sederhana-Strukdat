#by Reza Alvin
#22-1-21


image lapbasket = "lapbasket.jpg"
image kamarkos = "kamarkos.jpg"
image char_boy = "boy.png"
image char_boy:
    "boy.png"
    xalign 0.75
    yalign 0.5
    zoom 1.5

define i = Character("Boy", color="#f72d2d")

label start:
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
            jump Tidur
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
            jump gapeduli
            return

    label Tidur:
        hide char_boy with dissolve
        "Yes akhirnya tidur, bentar aja deh yaa"
    menu:
        "Gas aja dah capek banget, ntar malem aja belajarnya":
            call tidurlama
            return
        "Bentar aja ah, belom siap buat ujian besok":
            jump tidurBentar
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
                jump info
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
                jump contek
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
                jump belajarDulu
                return

    label tidurBentar:
        "bentar aja kali ya"
        "~~Kebangun pukul 7 malam"
        menu:
            "ah baru jam segini lanjut tidur aja deh":
                call lanjutTidur
                return
            "wah udah jam segini bangun dulu ah belajar":
                jump belajarDulu
                return

    label materi:
        "Wahh ternyata materi besok banyak nih pelajari atau pasrah sebisanya aja yaa? haha"
        menu:
            "Paksa Pelajari":
                call berhasil
                return
            "Sebisanya aja deh":
                jump gagal
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
                jump berhasil
                return

    label yakin:
        "Aduh itu kan materi yang baru kemaren dipelajarin gampang pasti"
        menu:
            "Kalo ada yang gabisa jawab sebisanya ajaa deh":
                call berhasil
                return
            "Kalo gabisa tinggal di asal aja jawabnya mah":
                jump gagal
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
                jump berhasil
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
                jump gagal
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
                jump berhasil
                return

    label berhasil:
        "-GAME OVER-
        Selamat pilihanmu akan berdampak dengan berhasil lulus ujian besok :D"
        return
    label gagal:
        "-GAME OVER-
        Yah pilihanmu bakal berdampak kamu gagal dalam ujian besok... ;("
        return
