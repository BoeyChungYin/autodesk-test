#include <iostream>
#include <string>
#include <algorithm>
#include <cassert>

// Function to reverse any word
std::string reverse_word(const std::string &word)
{
    std::string result = word;
    int left = 0, right = word.size() - 1;

    while (left < right){
        std::swap(result[left++], result[right--]);
    }

    return result;
}

std::string reverse_words(const std::string &str)
{
    std::string result;
    std::string buffer;

    for (char ch : str) {
        if (!std::isalnum(static_cast<unsigned char>(ch))) {
            // Reverse the buffer and empty it
            if (!buffer.empty()) {
                result += reverse_word(buffer);
                buffer.clear();
            }
            result += ch; // Append any non alphanumberic values
        } else {
            buffer += ch; // Fill buffer with alphanumeric values
        }
    }

    // Last word in the string
    if (!buffer.empty()) {
        result += reverse_word(buffer);
    }

    return result;
}

int main()
{
    std::string test_str1 = "String; 2be reversed...";
    assert(reverse_words(test_str1) == "gnirtS; eb2 desrever...");

    std::string test_str2 = "String; 2be rev!ersed...";
    assert(reverse_words(test_str2) == "gnirtS; eb2 ver!desre...");

    // For debugging
    std::string result = reverse_words(test_str2);
    std::cout << result << std::endl;

    return 0;
}