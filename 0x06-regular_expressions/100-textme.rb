#!/usr/bin/env ruby

# Define the regular expression pattern
pattern = /\[\s*from:(.*?)\s*\]\s*\[\s*to:(.*?)\s*\]\s*\[\s*flags:(.*?)\s*\]/

# Check if exactly one argument is passed
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} '<log_entry>'"
  exit 1
end

# Extract the log entry from the argument
log_entry = ARGV[0]

# Match the log entry against the regular expression pattern
matches = log_entry.match(pattern)

if matches
  # Extract the sender, receiver, and flags from the matched groups
  sender = matches[1]
  receiver = matches[2]
  flags = matches[3]

  # Output the result in the required format
  puts "#{sender},#{receiver},#{flags}"
else
  # Output "No match" if the log entry does not match the pattern
  puts "No match"
end
