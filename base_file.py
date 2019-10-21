import os
def chotdonhang():
    hoten_input = input('Nhap ho ten khach hang: ')
    diachi_input = input('Nhap dia chi: ')
    sdt_input = input('Nhap SDT: ')
    sanpham_input = input('Nhap san pham (nhap -1 de ket thuc): ')
    outfile = open('information.txt', 'w')
    new_data_hoten = 'Họ tên khách hàng: ' + str(hoten_input) + '\n'
    new_data_diachi = 'Địa chỉ: ' + str(diachi_input) + '\n'
    new_data_sdt = 'SĐT: ' + str(sdt_input) + '\n'
    outfile.write('Minh note lại nhe:' + '\n' + '\n')
    outfile.write(new_data_hoten)
    outfile.write(new_data_diachi)
    outfile.write(new_data_sdt + '\n')
    outfile.write('SẢN PHẨM:' + '\n')

    list_gia = []
    i = 0
    while sanpham_input != '-1':
        i = i + 1
        outfile.write(str(i) + '/ ' + sanpham_input.upper() + '\n')
        soluong_input = input('Nhap so luong: ')
        if int(soluong_input) > 1:
            giasanpham_input = input('Nhap gia: ')
            split_giasanpham = giasanpham_input.split('.')
            join_giasanpham = ''.join(split_giasanpham)
            bientinh = int(soluong_input) * int(join_giasanpham)
            bientinh_cham = '{:,}'.format(bientinh).replace(',', '.')
            list_gia.append(int(bientinh))
            outfile.write('Giá: ' + soluong_input + ' ' + 'x' + ' ' + giasanpham_input + 'đ' + ' ' + '=' + ' ' + str(bientinh_cham) + 'đ' + '\n' + '\n')
            sanpham_input = input('Nhap san pham (nhap -1 de ket thuc): ')
        elif soluong_input == '1':
            giasanpham_input = input('Nhap gia: ')
            outfile.write('Giá: ' + giasanpham_input + 'đ' + '\n' + '\n')
            split_giasanpham = giasanpham_input.split('.')
            join_giasanpham = ''.join(split_giasanpham)
            list_gia.append(int(join_giasanpham))
            sanpham_input = input('Nhap san pham (nhap -1 de ket thuc): ')
    sum_gia = 0
    sum_phi_ship = 0
    for j in range(0,len(list_gia)):
        sum_gia = sum_gia + int(list_gia[j])
    phiship_input = input('Mien phi ship ? (nhap 0 mien phi, nhap 1 nhap phi ship, nhap 2 ko bao phi ship) ')
    if phiship_input == '0':
        sum_gia_cham = '{:,}'.format(sum_gia).replace(',', '.')
        outfile.write('Số tiền: ' + str(sum_gia_cham) + 'đ' + '\n' + '\n')
        outfile.write('Miễn phí giao hàng' + '\n' + '\n')
    elif phiship_input == '1':
        tienship = input('Nhap tien ship hang: ')
        sum_gia_chamelif = '{:,}'.format(sum_gia).replace(',', '.')
        outfile.write('Tổng cộng: ' + str(sum_gia_chamelif) + 'đ' + '\n' + '\n')
        outfile.write('Phí ship: ' + tienship + 'đ' + '\n' + '\n')
        split_tienship = tienship.split('.')
        join_tienship = ''.join(split_tienship)
        sum_phi_ship = sum_gia + int(join_tienship)
        sum_phi_ship_cham = '{:,}'.format(sum_phi_ship).replace(',', '.')
        outfile.write('Số tiền: ' + str(sum_phi_ship_cham) + 'đ' + '\n' + '\n')
    elif phiship_input == '2':
        sum_gia_chamelifhai = '{:,}'.format(sum_gia).replace(',', '.')
        outfile.write('Tổng cộng: ' + str(sum_gia_chamelifhai) + 'đ' + '\n' + '\n')
        outfile.write('Không bao phí ship' + '\n' + '\n')
    outfile.write('Minh cảm ơn nhiều nha')
    outfile.close()
    infile = open('information.txt', 'r')
    data = infile.read()
    os.system("echo '%s' | pbcopy" % data)

chotdonhang()