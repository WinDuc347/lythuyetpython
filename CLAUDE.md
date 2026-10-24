# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python learning materials** repository from KU Leuven Books, containing exercises organized by 10+ sessions. Each session covers progressively more complex Python concepts, from basic functions and control flow to more advanced topics.

### Repository Structure

```
Python Thinking/
├── Session 2-10/        # Exercise files organized by session
│   ├── Exercise X.Y.py
│   ├── Difficult Tasks.py
│   ├── Extra Exercises.py
│   └── *.md files       # Explanations and notes
├── output/              # Generated solution files (markdown format)
├── Mock Exam.py         # Exam preparation files
└── CLAUDE.md           # This file
```

## Key Instructions

When working with this repository:

1. **Trả lời bằng tiếng Việt**: Toàn bộ đáp án và giải thích phải bằng tiếng Việt
2. **Xuất ra file.md**: Tạo file markdown (.md) cho các bài tập/giải thích
3. **Thêm footer**: Ở dưới mỗi file markdown, thêm dòng "Cảm ơn chủ nhân"
4. **Lưu vào output folder**: Lưu các file kết quả vào `Python Thinking/output/` folder

## Running Code

To run and test Python files:

```powershell
# Run a single exercise file
python "Session X/Exercise X.Y.py"

# Run all tests in a session
python "Session X/*.py"

# Test a specific function from file
python -c "from 'Session X.Exercise X.Y' import function_name; print(function_name(args))"
```

## Common Patterns

- Each exercise file typically contains multiple functions (labeled a, b, c, etc.)
- Tests are usually at the bottom of each file (print statements)
- Some exercises build on previous ones (check session notes for context)
- Explanatory .md files provide context for complex exercises

## Notes for Future Work

- Check if output folder exists before creating files
- Maintain consistent Vietnamese terminology across explanation files
- Review existing .md files in sessions for terminology and naming conventions