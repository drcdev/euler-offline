import 'dart:io';
import 'package:args/args.dart';

main(List<String> args) async {
  var parser = ArgParser();
  parser.addOption('number', abbr: 'n');
  final int number = int.tryParse(parser?.parse(args)['number'] ?? '');
  final String numberString = number.toString().padLeft(4, '0');
  if (number == null) {
    print("Invalid argument: please specify a number");
    return;
  }
  String filePath = 'inProgress/euler$numberString.dart';
  if (await File(filePath).exists()) {
    print('$filePath already exists');
    return;
  }
  String solution = '';
  final solutions = File('project_euler_problems.txt').readAsLinesSync();
  int index = 0;
  bool foundProblem = false;
  do {
    if (!foundProblem) {
      if (solutions[index].contains('Problem $number')) {
        foundProblem = true;
      }
    } else {
      if (solutions[index].contains('Answer:')) {
        solution = solutions[index].replaceAll('Answer:', '').trim();
        break;
      }
    }
    index += 1;
  } while (index < solutions.length);

  File(filePath).create(recursive: true).then((File file) {
    file.writeAsStringSync(
      'import "dart:convert";\n'
      'import "package:crypto/crypto.dart";\n'
      '\n'
      'main() {\n'
      '  String answer = solve();\n'
      '  String answerMd5 = generateMd5(answer);\n'
      '  print(\'Problem $numberString\');\n'
      '  print(\'Answer: \$answer\');\n'
      '  print(answerMd5);\n'
      '  print(checkAnswer(1, answerMd5));\n'
      '}\n'
      '\n'
      'String generateMd5(String input) {\n'
      '  return md5.convert(utf8.encode(input)).toString();\n'
      '}\n'
      '\n'
      'bool checkAnswer(int number, String answer) {\n'
      'String solution = \'$solution\';\n'
      'return answer == solution;\n'
      '}\n'
      '\n'
      'String solve() {\n'
      '  return "answer";\n'
      '}\n',
    );
  });
}
