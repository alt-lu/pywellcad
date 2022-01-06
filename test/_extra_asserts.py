__unittest = True

class ExtraAsserts:
    def assertAttrEqual(self, obj, name, value):
        """Tests if an object attribute is equal to some value."""
        self.assertEqual(getattr(obj, name), value)

    def assertAttrChange(self, obj, name, value):
        """Tests setting an attribute to some value and back again."""
        original = getattr(obj, name)
        setattr(obj, name, value)
        self.assertEqual(getattr(obj, name), value)
        setattr(obj, name, original)
        self.assertEqual(getattr(obj, name), original)

    def assertAttrAlmostChange(self, obj, name, value, *args, **kwargs):
        """Tests setting an attribute to some value and back again."""
        original = getattr(obj, name)
        setattr(obj, name, value)
        self.assertAlmostEqual(getattr(obj, name), value, *args, **kwargs)
        setattr(obj, name, original)
        self.assertAlmostEqual(getattr(obj, name), original, *args, **kwargs)
    
    def assertAttrNotChanged(self, obj, name, value):
        """Tests whether setting an attribute to some value does not change it."""
        original = getattr(obj, name)
        setattr(obj, name, value)
        new = getattr(obj, name)
        if new != original:
            # It did change, so let's set it back for now and raise.
            setattr(obj, name, original)
            raise AssertionError(f"Attribute {name} changed from {original} to {new} when it shouldn't have.")

    def assertAttrChangeRaises(self, obj, name, value):
        """Tests whether setting an attribute raises an exception."""
        original = getattr(obj, name)
        with self.assertRaises(Exception):
            try:
                setattr(obj, name, value)
            finally:
                setattr(obj, name, original)