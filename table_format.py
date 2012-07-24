# Copyright 2012 Google Inc. All Rights Reserved.

"""Basic formatter for Shannonigans Temp data.

After aggregating all of the data, flag the issues and output a basic table that
contains the CCs in the rows and the type of issue in the columns.

"""

__author__ = 'tbowland@google.com (Taylor Bowland)'


def MakeTable(f_dict, headers):
  """Parse the incoming data and flag the issues.

  Args:
    f_dict: dictionary of dictionaries in the following format -
    | {
    |  row1: {col1: [values], col2: [values]},
    |  row2: {col1: [values], col2: [values]},
    |  row3: {col1: [values], col2: [values]}
    | }
    headers: list of table headers. The first argument can be anything, but the
      remaining arguments must match the columns in f_dict
  """

  # Create a dictionary of the column widths
  col_widths = {}
  col_headers = {}
  for index, header in enumerate(headers):
    max_len = len(header)
    if index > 0:
      # Iterate the values in each column of f_dict and set the column width
      # equal to the longest value + 3
      for key, value in f_dict.iteritems():
        for item in value[header]:
          if len(item) > max_len:
            max_len = len(item)
    else:
      for key in f_dict:
        if len(key) > max_len:
          max_len = len(key)
    col_widths['h%s' % index] = max_len + 3
    col_headers['t%s' % index] = header

  # Geneator the row separator
  separator = ''
  for i in range(0, len(headers)):
    separator += '+{spacer:-^{0[h%s]}s}' % i
    if i == len(headers) - 1:
      separator += '+'
  separator = separator.format(col_widths, spacer='')

  # Generate the printable column headers
  col_print = ''
  for i in range(0, len(headers)):
    col_print += '|{0[t%s]: ^{1[h%s]}s}' % (i, i)
    if i == len(headers) -1:
      col_print += '|'

  # Start printing
  print separator
  print col_print.format(col_headers, col_widths)
  print separator

  # Print the actual data
  for key, value in sorted(f_dict.iteritems()):
    value_fix, max_len = AdjustLengths(value)
    for i in range(0, max_len):
      # This prevents the row header from repeating
      if i > 0:
        key = ''
      row_print = '|{0: ^{2[h0]}s}'
      for index, header in enumerate(headers):
        if index > 0:
          row_print += '|{1[%s][%s]: ^{2[h%s]}s}' % (header, i, index)
        if index == len(headers) - 1:
          row_print += '|'

      print row_print.format(key, value_fix, col_widths)

    if max_len > 0:
      print separator


def AdjustLengths(data):
  """Adjust all cells so that they are of equal length.

  In order for this to function properly, all cells must have an equal
  number of elements. This adds null values to each cell until the len
  of the cell == max_len in the row.

  Args:
    data: the data to be parsed

  Returns:
    temp_dict: the same data but with null values added to cells so that all
               are of equal length
    max_len: the length of the longest cell
  """
  temp_dict = {}
  # Determine the maximum length of a cell in the row
  max_len = max([len(cc_issue) for cc_issue in data.values()])
  for issue, value in data.iteritems():
    # If this cell is shorter than the max_len, add '' until len == max_len
    if len(value) < max_len:
      temp = len(value)
      while temp < max_len:
        value.append('')
        temp += 1
    temp_dict[issue] = value

  return temp_dict, max_len
