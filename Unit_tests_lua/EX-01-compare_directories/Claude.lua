function compare_directories(dir1, dir2)

    local report = {
      Passed = true,
      Failed_Count = 0,
      Failed_Tests = {}
    }
  
    -- Loop through all files in dir1
    for _, file1 in ipairs(list_files(dir1)) do
  
      -- Get corresponding file in dir2
      local file2 = get_file(dir2, get_filename(file1))
  
      -- Compare files
      if file1.modified < file2.modified then
        -- File in dir1 is older
        report.Failed_Location = "dir1" 
      elseif file1.modified > file2.modified then
        -- File in dir2 is older
        report.Failed_Location = "dir2"
      end
  
      -- Check if files are identical
      if file1.content ~= file2.content then
        
        -- Update report
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
  
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1.name, file2.name},
          Failure_Location = report.Failed_Location
        })
  
      end
  
    end
  
    return report
  
  end