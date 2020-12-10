# coding: utf-8


def card_check_luhn(band_account):

    band_account = [int(x) for x in band_account]
    band_account.reverse()
    sub_bank_account = band_account[1:]

    total = 0
    for i in range(len(sub_bank_account)):
        if i % 2 == 0:
            k = sub_bank_account[i] * 2
            total += int(k / 10) + k % 10
        else:
            total += sub_bank_account[i]

    return 'PASS' if (total + band_account[0]) % 10 == 0 else str(10 - ((total + band_account[0]) % 10))


if __name__ == '__main__':

    card_no = '370286002029947'
    print(card_check_luhn(card_no))
