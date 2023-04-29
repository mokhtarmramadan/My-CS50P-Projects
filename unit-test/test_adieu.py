from adieu import output

def test_output():
    assert output(['Liesl']) == "Adieu, adieu, to Liesl"
    assert output(['Liesl', 'Friedrich']) == "Adieu, adieu, to Liesl and Friedrich"
    assert output(['Liesl']) == "Adieu, adieu, to Liesl"
    assert output(['Liesl', 'Friedrich', 'Louisa']) == "Adieu, adieu, to Liesl, Friedrich, and Louisa"