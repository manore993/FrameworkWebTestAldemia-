from common.common_fixture import common_fixture
from common.utils import SafePage
import random

register_url = "https://pprod.aldemia.fr/registrer/"
logout_url = "https://pprod.aldemia.fr/wp-login.php?action=logout"

def force_log_out(page):
    try: 
        page.page.goto(logout_url)
        page.click("a")
    except: 
        # Peut arriver si pas connecté
        pass

def test_inscription(common_fixture: SafePage):
    page = common_fixture

    #Le block pour extraire test name and requirement (class test_case_requirement or test_details)
    test_case_reference = "CT_INS_001"
    test_case_name = "Vérification de l'accès au formulmaire d'inscription"
    test_case = f"{test_case_reference} - {test_case_name}"
    requirement = "Inscription"
    #Le block pour extraire test name and requirement

    page.set_test_details(test_case, requirement)

    force_log_out(page)
    page.page.goto(register_url)

    random_suffix = random.randint(1, 100000000)

    page.fill("#rpress-user-login", f"toto_{random_suffix}", field_name="nom d'utilisateur")
    page.fill("#rpress-user-email", f"toto_{random_suffix}@gmail.com", field_name="email")
    page.fill("#rpress-user-pass", "AZERTY123", field_name="mot de passe")
    page.fill("#rpress-user-pass2", "AZERTY123", field_name="mot de passe (confirmation)")
    page.click("#rpress-purchase-button", field_name="inscription")

    page.verify_visible("Vous n'avez passé aucune commande")

def test_inscription_invalide_email(common_fixture: SafePage):
    page = common_fixture

    #Le block pour extraire test name and requirement (class test_case_requirement or test_details)
    test_case_reference = "CT_INS_001"
    test_case_name = "Vérification de l'accès au formulmaire d'inscription"
    test_case = f"{test_case_reference} - {test_case_name}"
    requirement = "Inscription"
    #Le block pour extraire test name and requirement

    page.set_test_details(test_case, requirement)

    force_log_out(page)
    page.page.goto(register_url)

    random_suffix = random.randint(1, 100000000)

    page.fill("#rpress-user-login", f"toto_{random_suffix}", field_name="nom d'utilisateur")
    page.fill("#rpress-user-email", f"toto_{random_suffix}@gmail", field_name="email")
    page.fill("#rpress-user-pass", "AZERTY123", field_name="mot de passe")
    page.fill("#rpress-user-pass2", "AZERTY123", field_name="mot de passe (confirmation)")
    page.click("#rpress-purchase-button", field_name="inscription")

    page.verify_visible("Email invalide")