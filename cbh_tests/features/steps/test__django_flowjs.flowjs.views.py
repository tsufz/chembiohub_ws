from behave import given, when, then
import json

from django.db import IntegrityError

@given("I upload a file to django flowjs")
def step(context):
    """Note that here we use the django client rather than the tastypie client"""
    from django.conf import settings
    with open("cbh_tests/test_image.png") as f:
        context.flowfilepostresp = context.api_client.client.post("/" + settings.WEBSERVICES_NAME + "/flow/upload/", {"file": f, "flowChunkNumber": 1, 
            "flowChunkSize": 22222222, 
            "flowCurrentChunkSize": 137227,
            "flowTotalSize": 137227,
            "flowFilename": "test_image.png",
            "flowIdentifier": "137227-test_image.png",
            "flowRelativePath": "test_image.png",
            "flowTotalChunks": 1})




@given("I upload a spreadsheet to flowfiles")
def step(context):
    with open("src/cbh_datastore_ws/cbh_datastore_ws/features/fixtures/sample_data.xlsx") as f:
        resp = context.dclient.post("/dev/api/flow/upload/", {"file": f, "flowChunkNumber": 1, 
            "flowChunkSize": 22222222, 
            "flowCurrentChunkSize": 137227,
            "flowTotalSize": 137227,
            "flowFilename": "newtest.xlsx",
            "flowIdentifier": "137227-newtestxlsx",
            "flowRelativePath": "newtest.xlsx",
            "flowTotalChunks": 1})
    resp = context.api_client.get("/dev/api/datastore/cbh_flowfiles/137227-newtestxlsx", 
        format="json", 
        follow=True)




@when("I GET the file object via the URI from the (made up) session ID")
def step(context):
    from django.conf import settings
    context.flowfilegetresp = context.api_client.get("/" + settings.WEBSERVICES_NAME + "/datastore/cbh_flowfiles/137227-test_image.png", 
    format="json", 
    follow=True)


@then("The file has been created and the file details can be retrieved from the server")
def step(context):
    from django.conf import settings
    context.test_case.assertHttpOK(context.flowfilegetresp)
    context.test_case.assertHttpOK(context.flowfilepostresp)


@given(u'A flowfile object is created from the front end')
def step_impl(context):
    context.execute_steps(u"""
                Given I upload a file to django flowjs
        When I GET the file object via the URI from the (made up) session ID
        Then The file has been created and the file details can be retrieved from the server
        """)

@when(u'I combine the flowfile id with the parent data point classification')
def step_impl(context):
    from django.conf import settings
    l0 = json.loads(context.l0_resp.content)
    
    context.image_attachment_data = {
        "flowfile": "/" + settings.WEBSERVICES_NAME + "/datastore/cbh_flowfiles/137227-test_image.png",
        "data_point_classification": l0["resource_uri"],
        "chosen_data_form_config" : context.l1_uri
    }



@given("An attachment object is saved by an owner of the project")
def step_impl(context):
    context.execute_steps(u"""
        Given I create a datapoint classification as before
        and A flowfile object is created from the front end
        When I list the nested datapoint classifications in the project
        and I combine the flowfile id with the parent data point classification
        and POST the attachment object to the base attachment API
        Then the attachment object has been created
        When I make a request to the raw image url
        Then the raw url delivers a response in png format
        """)

@when(u'POST the attachment object to the base attachment API')
def step_impl(context):
    from django.conf import settings
    context.attachment_resp = context.api_client.post("/" + settings.WEBSERVICES_NAME + "/datastore/cbh_base_attachments", data=context.image_attachment_data)
    print(context.attachment_resp.content)

@then(u'the attachment object has been created')
def step_impl(context):
    context.test_case.assertHttpCreated(context.attachment_resp)

@then("the attachment object is not created as unauthorized")
def step_impl(context):
    context.test_case.assertHttpUnauthorized(context.attachment_resp)

@when("I make a request to the raw image url")
def step_impl(context):
    ff_data = json.loads(context.attachment_resp.content)
    context.image = context.api_client.client.get(ff_data["resource_uri"])


@then(u'the raw url delivers a response in png format')
def step_impl(context):
    context.test_case.assertEquals(context.image.get("content-type"), "image/png")
    context.test_case.assertHttpOK(context.image)



@then(u'the request to the raw url is rejected as unauthorized')
def step_impl(context):
    context.test_case.assertHttpUnauthorized(context.image)