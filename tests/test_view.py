from calculate.view import View


def test_menu(capsys):
    View.print_menu()
    out, err = capsys.readouterr()
    expected_output = (
        "\n=========== MENU ==========="
        "\n1 - Addition"
        "\n2 - Soustraction"
        "\n3 - Multiplication"
        "\n4 - Division"
        "\n5 - Quitter"
        "\n============================\n\n"
    )
    assert out == expected_output, "Test Menu"


def test_end_message(capsys):
    View.end_message()
    out, err = capsys.readouterr()
    expected_output = "=========== GOOD-BYE ===========\n"
    assert out == expected_output



