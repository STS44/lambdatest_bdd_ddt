import allure
from pytest_bdd import given, when, then, scenarios, parsers

from utils.converters import json_to_dict
from utils.file_utils import read_data_file

scenarios("lambdatest.feature")


@given(
    parsers.parse("a JSON file is prepared: {json_file_name}"), target_fixture="context"
)
def a_json_file_is_prepared(json_file_name, context):
    with allure.step("Prepare JSON file"):
        input_json = read_data_file(f"json/{json_file_name}.json")
        context["json"] = input_json
        return context


@given(
    parsers.parse("a TXT file is prepared: {txt_file_name}"), target_fixture="context"
)
def a_txt_file_is_prepared(txt_file_name, context):
    with allure.step("Prepare TXT file"):
        expected_text = read_data_file(f"txt/{txt_file_name}.txt")
        context["txt"] = expected_text
        return context


@given(
    parsers.parse("a XML file is prepared: {xml_file_name}"), target_fixture="context"
)
def a_xml_file_is_prepared(lambdatest_service, xml_file_name, context):
    with allure.step("Prepare XML file"):
        input_xml = read_data_file(f"xml/{xml_file_name}.xml")
        context["xml"] = input_xml
        return context


@given("a mini XML is prepared from XML file", target_fixture="context")
def a_mini_xml_is_prepared(lambdatest_service, context):
    with allure.step("Prepare mini XML"):
        input_xml = context["xml"]
        expected_mini_xml = lambdatest_service.minify_xml(input_xml)
        context["mini_xml"] = expected_mini_xml
        return context


@given(
    parsers.parse("a YAML file is prepared: {yaml_file_name}"), target_fixture="context"
)
def a_yaml_file_is_prepared(yaml_file_name, context):
    with allure.step("Prepare YAML file"):
        input_yaml = read_data_file(f"yaml/{yaml_file_name}.yaml")
        context["yaml"] = input_yaml
        return context


@given("a dict is prepared from JSON file", target_fixture="context")
def a_dict_is_prepared(context):
    with allure.step("Prepare dict from JSON"):
        input_json = context["json"]
        expected_dict = json_to_dict(input_json)
        context["dict"] = expected_dict
        return context


@when("the text is extracted from JSON", target_fixture="context")
def text_extracted_from_json(lambdatest_service, context):
    with allure.step("Extract text from JSON via API"):
        input_json = context["json"]
        actual_text = lambdatest_service.extract_text_from_json(input_json)
        context["actual_txt"] = actual_text
        return context


@when("JSON is converted to XML", target_fixture="context")
def json_converted_to_xml(lambdatest_service, context):
    with allure.step("Convert JSON to XML via API"):
        input_json = context["json"]
        actual_mini_xml = lambdatest_service.json_to_xml(input_json)
        context["actual_mini_xml"] = actual_mini_xml
        return context


@when("YAML is validated", target_fixture="context")
def yaml_validated(lambdatest_service, context):
    with allure.step("Validate YAML via API"):
        input_yaml = context["yaml"]
        actual_message = lambdatest_service.validate_yaml(input_yaml)
        context["actual_message"] = actual_message
        return context


@when("YAML is converted to JSON", target_fixture="context")
def yaml_converted_to_json(lambdatest_service, context):
    with allure.step("Convert YAML to JSON via API"):
        input_yaml = context["yaml"]
        actual_dict = lambdatest_service.yaml_to_json(input_yaml)
        context["actual_dict"] = actual_dict
        return context


@when("JSON is converted to YAML", target_fixture="context")
def json_converted_to_yaml(lambdatest_service, context):
    with allure.step("Convert JSON to YAML via API"):
        input_json = context["json"]
        actual_yaml = lambdatest_service.json_to_yaml(input_json)
        context["actual_yaml"] = actual_yaml
        return context


@when("YAML is converted to XML", target_fixture="context")
def yaml_converted_to_xml(lambdatest_service, context):
    with allure.step("Convert YAML to XML via API"):
        input_yaml = context["yaml"]
        actual_mini_xml = lambdatest_service.yaml_to_xml(input_yaml)
        context["actual_mini_xml"] = actual_mini_xml
        return context


@when("XML is converted to YAML", target_fixture="context")
def xml_converted_to_yaml(lambdatest_service, context):
    with allure.step("Convert XML to YAML via API"):
        input_xml = context["xml"]
        actual_yaml = lambdatest_service.xml_to_yaml(input_xml)
        context["actual_yaml"] = actual_yaml
        return context


@then("the extracted text is equal to the text from TXT file")
def text_returned_match_expected(context):
    with allure.step("Compare expected and actual text"):
        actual_text = context["actual_txt"]
        expected_text = context["txt"]
        assert actual_text == expected_text


@then("converted JSON is equal to mini XML")
def converted_json_match_expected_mini_xml(context):
    with allure.step("Compare expected and actual mini XML"):
        actual_mini_xml = context["actual_mini_xml"]
        expected_mini_xml = context["mini_xml"]
        assert actual_mini_xml == expected_mini_xml


@then(parsers.parse("the {message} appears"), target_fixture="context")
def message_match_expected(context, message):
    with allure.step("Compare expected and actual message"):
        actual_message = context["actual_message"]
        expected_message = f"{message}"
        assert actual_message == expected_message


@then("converted YAML is equal to dict from JSON file", target_fixture="context")
def converted_yaml_match_expected_dict(context):
    with allure.step("Compare expected and actual dict"):
        actual_dict = context["actual_dict"]
        expected_dict = context["dict"]
        assert actual_dict == expected_dict


@then("converted JSON is equal to YAML from YAML file", target_fixture="context")
def converted_json_match_expected_yaml(context):
    with allure.step("Compare expected and actual yaml"):
        actual_yaml = context["actual_yaml"]
        expected_yaml = context["yaml"]
        assert actual_yaml == expected_yaml


@then("converted YAML is equal to mini XML", target_fixture="context")
def converted_yaml_match_mini_xml(context):
    with allure.step("Compare expected and actual mini XML"):
        actual_mini_xml = context["actual_mini_xml"]
        expected_mini_xml = context["mini_xml"]
        assert actual_mini_xml == expected_mini_xml


@then("converted XML is equal to YAML from a YAML file", target_fixture="context")
def converted_xml_match_expected_yaml(context):
    with allure.step("Compare expected and actual YAML"):
        actual_yaml = context["actual_yaml"]
        expected_yaml = context["yaml"]
        assert actual_yaml == expected_yaml
