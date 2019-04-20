from src import create_st


def test_read_type():
    input_type = {"var" : "int", "boo" : "int"}
    output = create_st.read_type(input_type)
    assert output == ['int', 'int']


def test_create_st():
    input_type = ['int', 'int']
