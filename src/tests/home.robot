*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Main Page Should Be Open
    Title Should Be   BibTeX-viittaus generaattori

Can Navigate To RefForm And Back
    Click Element  id:refFormLink
    Title Should Be  Viittaus Lomake
    Click Element  id:frontPageLink
    Title Should Be   BibTeX-viittaus generaattori

*** Keywords ***
Go To Main Page
    Go To  ${HOME URL}
