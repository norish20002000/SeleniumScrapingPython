  require "nokogiri"
  require "pp"
  
  
  # input: HTML String
  # output: HTML String の二次元配列
  
  
  def copy_rowspan_content
      $html_in_row << $rowspan_count[$html_in_row.length]["content"]
      $rowspan_count[$html_in_row.length - 1]["remaining_rowspan"] -= 1
      if $rowspan_count[$html_in_row.length - 1]["remaining_rowspan"] == 0
        $rowspan_count.delete($html_in_row.length - 1)
      end
  end
  
  def record(rowspan_value)
    $rowspan_count[$html_in_row.length] = {"remaining_rowspan" => rowspan_value - 1, "content" => $cell_node.inner_html}
  end
  
  def record_rowspan(rowspan_value, colspan)
    if rowspan_value > 1
      record(rowspan_value)
      unless colspan.nil?
        (colspan.value.to_i - 1).times do
          $html_in_row << $cell_node.inner_html
          record(rowspan_value)
        end
      end
    end
  end
  
  def row_to_array(row)
    node_index = 0
    cell_nodeset = row.css("th,td")
    $html_in_row = []
    until (cell_nodeset.nil? or node_index >= cell_nodeset.length) and $rowspan_count[$html_in_row.length].nil?
      unless $rowspan_count[$html_in_row.length].nil?
        copy_rowspan_content
      else
        $cell_node = cell_nodeset[node_index]
        rowspan = $cell_node.attribute("rowspan")
        colspan = $cell_node.attribute("colspan")
        if not rowspan.nil?
          record_rowspan(rowspan.value.to_i, colspan)
        elsif not colspan.nil?
          (colspan.value.to_i - 1).times do
            $html_in_row << $cell_node.inner_html
          end
        end
        $html_in_row << $cell_node.inner_html
        node_index += 1
      end
    end 
    return $html_in_row
  end
  
  def table_to_array(table)
    begin
      doc = Nokogiri::HTML.parse(table)
    rescue => e
      puts "parse error"
    end
    $rowspan_count = {}
    html_in_table = []
    row_nodeset = doc.css("tr")
    row_nodeset.each do |row|
      html_in_table << row_to_array(row)
    end
    return html_in_table
  end
  
  if __FILE__ == $0
    table_sample = DATA.read
    pp table_to_array(table_sample)
  end
  
  __END__
  <table>
      <tr>
          <th>Table name</th>
          <th>Col1</th>
          <th>Col2</th>
          <th>Col3</th>
          <th>Col4</th>
          <th>Col5</th>
      </tr>
      <tr>
          <th>Row1</th>
          <td>cell1_1</td>
          <td>cell1_2</td>
          <td>cell1_3</td>
          <td>cell1_4</td>
          <td>cell1_5</td>
      </tr>
      <tr>
          <th>Row2</th>
          <td>cell2_1</td>
          <td colspan=2>cell2_2 cell2_3</td>
          <td>cell2_4</td>
          <td>cell2_5</td>
      </tr>
      <tr>
          <th>Row3</th>
          <td>cell3_1</td>
          <td>cell3_2</td>
          <td>cell3_3</td>
          <td>cell3_4</td>
          <td rowspan=2>cell3_5<br>cell4_5</td>
      </tr>
      <tr>
          <th>Row4</th>
          <td colspan=2 rowspan=2>cell4_1 cell4_2<br>cell5_1 cell5_2</td>
          <td>cell4_3</td>
          <td>cell4_4</td>