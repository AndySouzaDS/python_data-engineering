"""**************************************************************************************************************************************************************
goal of this course is to transform you into a Python expert, and so the first chapter starts off with best practices when writing functions.
You'll cover docstrings and why they matter and how to know when you need to turn a chunk of code into a function. You will also learn the details of how Python passes 

Docstrings
==========
- makes your code easier to use, read, maintain

    @ anatomy of docstring
    -----------------------
      def func_name(arguments):
        '''
         Description of what it does 
         Description of argument(s) if any
         Description of return value(s) if any
         Description of errors raised if any
         Optional extra notes or examples
         '''
    @ docstring Formats
    -----------------------     
    - Google style (pupular)  - NumpyDoc (popular)  - reStructuredText    - EpyText
    
      ----Google style === straight to the point eg. '''Stack the columns''' and just Arg:, Raises: , Returns: , Notes:
      ----NumpyDoc     === more vertical with line tittles, takes more space
      
    @ Review Documentation
    -----------------------
    >>>>>>>> func_name.__doc__ ====review documentation
    >>>>>>>> .getdoc(dunc_name) (inspect module)
    
        ++
            import inspect
            print(inspect.getdoc(func_name))
**************************************************************************************************************************************************************"""
## Crafting a docstring

# Add a docstring to count_letter()
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.
  
  # Add a Google style arguments section
  Args:
    content (str): The string to search.
    letter (str): The letter to search for.
    
  # Add a returns section
  Returns:
    int
    
  # Add a section detailing what errors might be raised
  Raises:
    ValuError: If `letter` is not a one-character string
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

