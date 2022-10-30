from MyQR import myqr as mq

def make_qr(url):
    domen_lists = ['.com', '.ru', '.uz', '.org', '.net', '.int', '.edu', '.gov',
                   '.mil', '.arpa', '.top', '.me', '.app', '.io', 'dev', '.html']
    there = False

    for domen in domen_lists:
        if domen in url.lower():
            there = True
            break

    if there:
        text = url.replace(".", '')
        text = text.replace("https://", '')
        text = text.replace('/', '')
        photo = f"images/{text}.jpg"
        try:
            mq.run(url, save_name=photo)
            return photo
        except:
            return False

    elif url[0] == '@':
        isstr = url.replace('_', '')
        isstr = isstr.replace('@', '')
        if isstr.isalnum():
            text = url.replace('@', '')
            url = 'https://t.me/' + text
            photo = f"images/{text}.jpg"
            mq.run(url, save_name=photo)
            return photo

    else:
        return False

if __name__ == '__main__':
    pass
    # make_qr("@Rahimov_Ilhomjon")
    # make_qr('topcoder.com')
    # print(make_qr('ilhomjon d'))