Feature: Employee Claims Management in OrangeHRM
    As an HR administrator
    I want to manage employee claims
    So that I can efficiently process employee expense reimbursements

    Background:
        Given I am on the OrangeHRM login page
        When I login with valid credentials
        Then I should be redirected to the dashboard

    @assign_claims
    Scenario: Assign and manage employee travel allowance claim
        Given I navigate to the Claims section
        When I click on Employee Claims
        And I add a new Assign Claim with employee "Amelia Brown", event "Travel Allowance", and currency "Euro"
        Then I should see success message "Successfully Saved"
        And I should be redirected to Assign Claim details page
        And the claim details should match the entered data
        When I add an expense with type "Accommodation", date "2025-11-25", and amount "150.00"
        Then I should see success message "Successfully Saved" for expense
        And the expense details should match the entered data
        When I click the Back button
        Then I should see the newly created claim in the records list