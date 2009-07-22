
from windmill.conf import global_settings
ADMIN_WIDGET_URL =  "%s/widget_admin/" % global_settings.TEST_URL
from windmill.authoring import WindmillTestClient
from django.test.utils import calling_func_name


def test_baseWidgetTestCars():
    client = WindmillTestClient("A second module")
    
    client.open(url=ADMIN_WIDGET_URL)
    client.waits.forPageLoad(timeout=u'20000')
    client.type(text=u'super', id=u'id_username')
    client.type(text=u'secret', id=u'id_password')
    client.click(value=u'Log in')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Car tires', timeout=u'8000')
    client.click(link=u'Car tires')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'              Add car tire             ', timeout=u'8000')
    client.click(link=u'              Add car tire             ')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(timeout=u'8000', id=u'id_car')
    client.click(id=u'id_car')
    client.click(xpath=u"//a[@id='add_id_car']/img")
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(xpath=u"//form[@id='car_form']/div/fieldset/div[2]/div", timeout=u'8000')
    client.click(xpath=u"//form[@id='car_form']/div/fieldset/div[2]/div")
    client.click(id=u'id_owner')
    client.select(option=u'super', id=u'id_owner')
    client.click(value=u'100')
    client.click(id=u'id_make')
    client.type(text=u'Ferrari', id=u'id_make')
    client.type(text=u'F-xx', id=u'id_model')
    client.click(xpath=u"//form[@id='car_form']/div/fieldset/div[2]")
    client.click(name=u'_save')
    client.waits.forPageLoad(timeout=u'20000')
    client.closeWindow()
    client.click(link=u'Home')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Car tires', timeout=u'8000')
    client.click(link=u'Car tires')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'              Add car tire             ', timeout=u'8000')
    client.click(link=u'              Add car tire             ')
    client.waits.forPageLoad(timeout=u'20000')
    client.select(option=u'Ferrari F-xx', id=u'id_car')
    client.click(value=u'1')
    client.click(name=u'_save')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'CarTire object', timeout=u'8000')
    client.click(link=u'CarTire object')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertImageLoaded(xpath=u"//a[@id='add_id_car']/img")
    client.asserts.assertNode(id=u'id_car')
    client.asserts.assertNode(link=u'Delete')
    client.click(xpath=u"//form[@id='cartire_form']/div/fieldset/div/div")
    client.click(link=u'Home')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Cars', timeout=u'8000')
    client.click(link=u'Cars')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertImageLoaded(xpath=u"//a[@id='add_id_form-0-owner']/img")
    client.asserts.assertNode(link=u'Ferrari')
    client.asserts.assertNode(id=u'id_form-0-owner')
    #client.asserts.assertSelected(xpath=u"//select[@id='id_form-0-owner']/option[3]", validator=u'')
    client.click(link=u'        Home       ')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(timeout=u'8000', id=u'user-tools')
    client.click(id=u'user-tools')
    client.click(link=u'Log out')
    client.waits.forPageLoad(timeout=u'20000')
    
def test_loginWidgetAdmin():
    '''Mostly just a proof of concept to test working order of tests.'''
    client = WindmillTestClient("freebie test")

    # print dir(client)
    #    print dir(client.open)
    #    print dir(client.commands)
    #    print client.commands()

    # client.open(url=ADMIN_URL)
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.type(text=u'super', id=u'id_username')
    #   client.type(text=u'secret', id=u'id_password')
    #   client.click(value=u'Log in')
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.asserts.assertNode(xpath=u"//div[@id='content-main']/div/table/tbody/tr[1]/th")
    #   client.asserts.assertNode(link=u'Articles')
    #   client.asserts.assertNode(link=u'Add')
    #   client.asserts.assertNode(link=u'Change')
    #   client.asserts.assertNode(link=u'Admin_Views')
    #   client.asserts.assertNode(xpath=u"//div[@id='user-tools']/strong")
    #   client.click(xpath=u"//div[@id='content-main']/div/table/tbody/tr[22]/td/a")
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.type(text=u'Test Section', id=u'id_name')
    #   client.click(name=u'_save')
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.asserts.assertNode(link=u'Section object')
    #   client.click(link=u'         Admin_views       ')
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.waits.forElement(link=u'Add', timeout=u'8000')
    #   client.click(link=u'Add')
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.type(text=u'Test 1', id=u'id_title')
    #   client.type(text=u'This is test content.', id=u'id_content')
    #   client.click(link=u'Today')
    #   client.click(link=u'Now')
    #   client.click(id=u'id_section')
    #   client.select(option=u'Section object', id=u'id_section')
    #   client.click(value=u'1')
    #   #client.asserts.assertValue(validator=u'2009-06-16', id=u'id_date_0')
    #   #client.asserts.assertValue(validator=u'13:31:21', id=u'id_date_1')
    #   client.asserts.assertNode(id=u'id_section')
    #   client.click(name=u'_save')
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.asserts.assertNode(link=u'This is test content.')
    #   client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[2]")
    #   client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[3]")
    #   client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[4]")
    #   client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[5]")
    #   client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/th")
    #   client.click(link=u'Today')
    #   client.waits.forPageLoad(timeout=u'20000')
    #   client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/th")
    #   client.click(link=u'        Home       ')
    #   client.waits.forPageLoad(timeout=u'20000')