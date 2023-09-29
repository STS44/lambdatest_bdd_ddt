Feature: Lambdatest

  Scenario Outline: Extract text from JSON
    Given a JSON file is prepared: <json_file_name>
    And a TXT file is prepared: <txt_file_name>
    When the text is extracted from JSON
    Then the extracted text is equal to the text from TXT file

    Examples:
      | json_file_name | txt_file_name |
      | 1              | 1             |
      | 2              | 2             |

  Scenario Outline: Convert JSON to XML
    Given a JSON file is prepared: <json_file_name>
    And a XML file is prepared: <xml_file_name>
    And a mini XML is prepared from XML file
    When JSON is converted to XML
    Then converted JSON is equal to mini XML

    Examples:
      | json_file_name | xml_file_name |
      | 1              | 1             |
      | 2              | 2             |

  Scenario Outline: Validate YAML
    Given a YAML file is prepared: <yaml_file_name>
    When YAML is validated
    Then the <message> appears

    Examples:
      | yaml_file_name | message    |
      | 1              | Valid YAML |
      | 2              | Valid YAML |

  Scenario Outline: Convert YAML to JSON
    Given a YAML file is prepared: <yaml_file_name>
    And a JSON file is prepared: <json_file_name>
    And a dict is prepared from JSON file
    When YAML is converted to JSON
    Then converted YAML is equal to dict from JSON file

    Examples:
      | yaml_file_name | json_file_name |
      | 1              | 1              |
      | 2              | 2              |

  Scenario Outline: Convert JSON to YAML
    Given a JSON file is prepared: <json_file_name>
    And a YAML file is prepared: <yaml_file_name>
    When JSON is converted to YAML
    Then converted JSON is equal to YAML from YAML file

    Examples:
      | json_file_name | yaml_file_name |
      | 1              | 1              |
      | 2              | 2              |

  Scenario Outline: Convert YAML to XML
    Given a YAML file is prepared: <yaml_file_name>
    And a XML file is prepared: <xml_file_name>
    And a mini XML is prepared from XML file
    When YAML is converted to XML
    Then converted YAML is equal to mini XML

    Examples:
      | yaml_file_name | xml_file_name |
      | 1              | 1             |
      | 2              | 2             |

  Scenario Outline: Convert XML to YAML
    Given a XML file is prepared: <xml_file_name>
    And a YAML file is prepared: <yaml_file_name>
    When XML is converted to YAML
    Then converted XML is equal to YAML from a YAML file

    Examples:
      | xml_file_name | yaml_file_name |
      | 1             | 1              |
      | 2             | 2              |
