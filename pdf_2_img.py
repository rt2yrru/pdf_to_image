import os
from pdf2image import pdfinfo_from_path,convert_from_path
def _start():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        _a=f.split('.')
        if(_a[-1]=='pdf'):
            _b=(_a[0].replace(' ','_'))
            print('Transferring Control To Pdf To Image')
            _pdf_2_img(_a[0],_b)
def _pdf_2_img(*k):
    print('Entered Pdf To Image')
    print(k[0],k[1])
    print(' Transferring Control To Delete Temp Ppm File')
    if not os.path.exists(k[1]):
        os.mkdir(k[1])
        print("Directory " , k[1],  " Created ")
    else:    
        print("Directory " , k[1],  " already exists")
    info=pdfinfo_from_path(k[0]+'.pdf')
    mxpg= info["Pages"]
    print(mxpg)
    _di=5
    for _b in range(1,mxpg,_di):

        images=convert_from_path(k[0]+'.pdf',first_page=_b,last_page=_b+_di-1,output_folder=k[1])
        for _i in range(0,len(images)):
            images[_i].save(k[1]+'/'+'page_'+ str(_i+_b) +'.jpg', 'JPEG')
            print(' Page ----> ',_b+_i)
        _remove_ppm(k)
def _remove_ppm(k):
    print(' removEd Ppm Files')
    for r, d, f in os.walk(k[1]):
        for _ in f:
            _a=_.split('.')
            if _a[-1]=='ppm':
                os.remove(k[1]+'/'+_)
                print(_)
_start()