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
  new File(filePath).create(recursive: true).then((File file) {
    file.writeAsStringSync(
      'import "dart:convert";\n'
      'import "package:crypto/crypto.dart";\n'
      '\n'
      'main() {\n'
      '  String answer = solve();\n'
      '  print(\'Problem $numberString\');\n'
      '  print(\'Answer: \$answer\');\n'
      '  print(generateMd5(answer));\n'
      '}\n'
      '\n'
      'String generateMd5(String input) {\n'
      '  return md5.convert(utf8.encode(input)).toString();\n'
      '}\n'
      '\n'
      'String solve() {\n'
      '  return "answer";\n'
      '}\n',
    );
  });
}
