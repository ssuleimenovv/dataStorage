import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def transform_text(text):
        words = text.split(' ')
        transformed_words = []
        for word in words:
            # Handle hyphenated words
            if '-' in word:
                parts = word.split('-')
                transformed_parts = []
                for part in parts:
                    if part:
                        transformed_parts.append(part[0].upper() + part[1:].lower())
                    else:
                        transformed_parts.append('')
                transformed_word = '-'.join(transformed_parts)
            else:
                if word:
                    transformed_word = word[0].upper() + word[1:].lower()
                else:
                    transformed_word = word
            transformed_words.append(transformed_word)
        return ' '.join(transformed_words)
    
    result = user_content.copy()
    result['original_text'] = result['content_text']
    result['converted_text'] = result['content_text'].apply(transform_text)
    return result[['content_id', 'original_text', 'converted_text']]