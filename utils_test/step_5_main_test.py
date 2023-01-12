from utils_test.step_5_conftest import test_client
class TestMain:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код"""
        response = test_client.get('/pain', follow_redirects=True)
        assert response.status_code == 404, "Статус-код неверный"

    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert "Это главная страничка" in response.data.decode("utf-8"), "Контент страницы неверный"