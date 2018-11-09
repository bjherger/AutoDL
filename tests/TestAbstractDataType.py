from keras_pandas.data_types.Abstract import AbstractDataType
from keras_pandas.lib import check_valid_datatype
from tests.testbase import TestBase


class TestAbstractDataType(TestBase):

    def test_output_support(self):
        datatype = AbstractDataType()
        datatype.supports_output = True
        self.assertTrue(check_valid_datatype(datatype))
        self.assertEqual(2, len(datatype.input_nub_generator('test', 'test')))
        self.assertEqual(None, datatype.output_nub_generator('test', 'test'))
        self.assertEqual(None, datatype.output_suggested_loss())
        self.assertTrue(datatype._check_output_support())

    def test_no_output_support(self):
        datatype = AbstractDataType()
        self.assertTrue(check_valid_datatype(datatype))
        self.assertEqual(2, len(datatype.input_nub_generator('test', 'test')))
        self.assertRaises(ValueError, datatype.output_nub_generator, 'test', 'test')
        self.assertRaises(ValueError, datatype.output_suggested_loss)
        self.assertRaises(ValueError, datatype._check_output_support)
