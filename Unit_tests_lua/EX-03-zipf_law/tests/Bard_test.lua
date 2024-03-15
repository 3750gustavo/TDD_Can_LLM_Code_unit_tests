local function zipfs_law(text)
    -- Remove punctuation and convert to lowercase
    local clean_text = string.gsub(text, "%p", "")
    clean_text = string.lower(clean_text)
  
    -- Split the text into words
    local words = string.split(clean_text)
  
    -- Create a table to store word counts
    local word_counts = {}
    for _, word in ipairs(words) do
      word_counts[word] = (word_counts[word] or 0) + 1
    end
  
    -- Sort the table by word count in descending order
    local sorted_words = {}
    for word, count in pairs(word_counts) do
      table.insert(sorted_words, {word = word, count = count})
    end
    table.sort(sorted_words, function(a, b) return b.count - a.count end)
  
    -- Return the top 10 most frequent words
    return table.sub(sorted_words, 1, 10)
  end

-- Define the local config table
  local config = {}

  config.string_input =
      [[toward it, and then stopped.
  
      There was a sound. A soft sliding sound. It stopped, then started again with a stealthy little bump. Everything inside me went loose. I regressed magically to four years of age. That sound wasn’t coming from the market. It was coming from behind me. From outside. Where the mist was. Something that was slipping and sliding and scraping over the cinderblocks. And, maybe, looking for a way in.
      
      Or maybe it was already in, and it was looking for me. Maybe in a moment I would feel whatever was making that sound on my shoe. Or on my neck.
      
      It came again. I was positive it was outside. But that didn’t make it any better. I told my legs to go and they refused the order. Then the quality of the noise changed. Something rasped across the darkness and my heart leaped in my chest and I lunged at that thin vertical line of light. I hit the doors straight-arm and burst through into the market.
      
      Three or four people were right outside the double doors—Ollie Weeks was one of them—and they all jumped back in surprise. Ollie grabbed at his chest. “David!” he said in a pinched voice. “Jesus Christ, you want to take ten years off my—” He saw my face. “What’s the matter with you?”
      
      “Did you hear it?” I asked. My voice sounded strange in my own ears, high and squeaking. “Did any of you hear it?”
      
      They hadn’t heard anything, of course. They had come up to see why the generator had gone off. As Ollie told me that, one of the bag-boys bustled up with an armload of flashlights. He looked from Ollie to me curiously.
      
      “I turned the generator off,” I said, and explained why.
      
      “What did you hear?” one of the other men asked. He worked for the town road department
      
      ; his name was Jim something.
      
      “I don’t know. A scraping noise. Slithery. I don’t want to hear it again.”
      
      “Nerves,” the other fellow with Ollie said.
      
      No. It was not nerves.
      
      “Did you hear it before the lights went out?”
      
      “No, only after. But...” But nothing. I could see the way they were looking at me. They didn’t want any more bad news, anything else frightening or off-kilter. There was enough of that already. Only Ollie looked as if he believed me.
      
      “Let’s go in and start her up again,” the bag-boy said, handing out the flashlights. Ollie took his doubtfully. The bag-boy offered me one, a slightly contemptuous shine in his eyes. He was maybe eighteen. After a moment’s thought, I took the light. I still needed something to cover Billy with.
      
      Ollie opened the doors and chocked them, letting in some light. The bleach cartons lay scattered around the half-open door in the plywood partition.
      
      The fellow named Jim sniffed and said, “Smells pretty rank, all right. Guess you were right to shut her down.”
      
      The flashlight beams bobbed and danced across cartons of canned goods, toilet paper, dog food. The beams were smoky in the drifting fumes the blocked exhaust had turned back into the storage area. The bag-boy trained his light briefly on the wide loading door at the extreme right.
      
      The two men and Ollie went inside the generator compartment. Their lights flashed uneasily back and forth, reminding me of something out of a boys’ adventure story—and I illustrated a series of them while I was still in college. Pirates burying their bloody gold at midnight, or
      
      maybe the mad doctor and his assistant snatching a body. Shadows, made twisted and monstrous by the shifting, conflicting flashlight beams, bobbed on the walls. The generator ticked irregularly as it cooled.
      
      The bag-boy was walking toward the loading door, flashing his light ahead of him. “I wouldn’t go over there,” I said.
      
      “No, I know you wouldn’t.”
      
      “Try it now, Ollie,” one of the men said. The generator wheezed, then roared.
      
      “Jesus! Shut her down! Holy crow, don’t that stink!”
      
      The generator died again.
      
      The bag-boy walked back from the loading door just as they came out. “Something’s plugged that exhaust, all right,” one of the men said.
      
      “I’ll tell you what,” the bag-boy said. His eyes were shining in the glow of the flashlights, and there was a devil-may-care expression on his face that I had sketched too many times as part of the frontispieces for my boys’ adventure series. “Get it running long enough for me to raise the loading door back there. I’ll go around and clear away whatever it is.”
      
      “Norm, I don’t think that’s a very good idea,” Ollie said doubtfully.
      
      “Is it an electric door?” the one called Jim asked.
      
      “Sure,” Ollie said. “But I just don
      
      't think it would be wise for—”
      
      “That’s okay,” the other guy said. He tipped his baseball cap back on his head. “I'll do it.” ]]
  
  config.first_6_words = {"the", "i", "and", "it", "of", "was"}
  config.valid_7th8th_words = {"a", "in"} -- any order
  config.valid_9th10th_words = {"that", "ollie", "said"} -- any order
  
  -- Function to retrieve the input text
  function config.get_string_input()
      return config.string_input
  end
  
  -- Define the function to generate a random string
  function config.generate_random_string(n)
      local random_string = ""
      local characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      for i = 1, n do
          local rand_index = math.random(#characters)
          random_string = random_string .. string.sub(characters, rand_index, rand_index)
      end
      return random_string
  end
  
  -- Define the function to generate a random string using text_generator
  function config.text_generator()
      return config.generate_random_string
  end
  
  function config.any_order_equal(word_to_check, expected_words_list)
      -- Check if the word is in the list of expected words
      for _, word in ipairs(expected_words_list) do
          if word == word_to_check then
              return true
          end
      end
      return false
    end

-- Test cases implemented
local input_text = config.get_string_input()
local top_words = zipfs_law(input_text)
-- variables to check if the test passed
local first_six_words_passed = true
local seventh_eighth_words_passed = true
local ninth_tenth_words_passed = true

for i, word in ipairs(top_words) do
  print(i .. ". " .. word.word)
  if i <= 6 then
      if word ~= config.first_6_words[i] then
          print("Test failed for word at index " .. i .. " - Expected: " .. config.first_6_words[i] .. ", Got: " .. word)
          first_six_words_passed = false
          -- Stop testing the first six words
          i = 7
      end
  elseif i <= 8 then
      if not config.any_order_equal(word, config.valid_7th8th_words) then
          print("Test failed for word at index " .. i .. " - Expected: " .. config.valid_7th8th_words[1] .. " or " .. config.valid_7th8th_words[2] .. ", Got: " .. word)
          seventh_eighth_words_passed = false
          -- Stop testing the 7th and 8th words
          i = 9
      end
  else
      if not config.any_order_equal(word, config.valid_9th10th_words) then
          print("Test failed for word at index " .. i .. " - Expected: " .. config.valid_9th10th_words[1] .. " or " .. config.valid_9th10th_words[2] .. ", Got: " .. word)
          ninth_tenth_words_passed = false
          -- Stop testing the 9th and 10th words
          i = 11
      end
  end
end

-- Function to print test results
local function printTestResults(first_six_words_passed, seventh_eighth_words_passed, ninth_tenth_words_passed)
  if first_six_words_passed then
    print("Test passed for first six words")
  else
    print("Test failed for first six words")
  end
  if seventh_eighth_words_passed then
    print("Test passed for 7th and 8th words")
  else
    print("Test failed for 7th and 8th words")
  end
  if ninth_tenth_words_passed then
    print("Test passed for 9th and 10th words")
  else
    print("Test failed for 9th and 10th words")
  end
end

-- Call the function with the test results
printTestResults(first_six_words_passed, seventh_eighth_words_passed, ninth_tenth_words_passed)

-- Performance section
local function performance_test(input_string,size)
  -- Warm-up
  for i = 1, 100 do
      zipfs_law(input_string)
  end
  -- Actual test
  local start_time = os.clock()
  for i = 1, size do
      zipfs_law(input_string)
  end
  local end_time = os.clock()
  -- Calculate average runtime in milliseconds
  local total_time = (end_time - start_time) * 1000
  local avg_time = total_time / size
  return avg_time
end

local input_string = config.get_string_input()
-- Run the tests
io.write("Do you want to run the performance test? (y/n): ")
local run_performance_test = io.read()
if run_performance_test == "y" then
    print("Performance test: ", performance_test(input_string,100000) .. " milliseconds")
end

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-03-zipf_law\tests\Bard_test.lua"