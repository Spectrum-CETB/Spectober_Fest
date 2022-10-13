import 'dart:async';
import 'dart:math';

import 'package:assets_audio_player/assets_audio_player.dart';
import 'package:confetti/confetti.dart';
import 'package:flutter/material.dart';
import 'package:tictoe/utils.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: const Splash(),
    );
  }
}


class Splash extends StatefulWidget {
  const Splash({Key? key}) : super(key: key);

  @override
  State<Splash> createState() => _SplashState();
}

class _SplashState extends State<Splash> {
  final controller1=TextEditingController();
  final controller2=TextEditingController();
  Color shadowcolor3=Colors.red;
  AssetsAudioPlayer audioPlayer = AssetsAudioPlayer();
  @override
  void initState() {
    super.initState();
    audioPlayer.open(
        Audio('assets/win.mp3'), autoStart: false, showNotification: false);

  }
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home:Scaffold(body:
SingleChildScrollView(child:
        Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        decoration: BoxDecoration(
        color: Colors.black,

    ),
    child:
    Column(
    children: [
    Padding(padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.13,bottom: 12,left: 12,right:12)),
    Container(
    height:MediaQuery.of(context).size.height*0.8,
    width: MediaQuery.of(context).size.width*0.9,
    clipBehavior: Clip.none,
    decoration: BoxDecoration(
    color:Colors.black,

    //Border.all

    borderRadius: BorderRadius.only(
    topLeft: Radius.circular(20.0),
    topRight: Radius.circular(20.0),
    bottomLeft: Radius.circular(20.0),
    bottomRight: Radius.circular(20.0),
    ),
    boxShadow: [
    BoxShadow(
    color: Colors.grey,
    offset: const Offset(
    5.0,
    5.0,
    ),
    blurRadius: 10.0,
    spreadRadius: 1.0,
    ),
    BoxShadow(
    color: Colors.grey,
    offset: const Offset(
    -5.0,
    -5.0,
    ),
    blurRadius: 10.0,
    spreadRadius: 1.0,
    ),//BoxShadow
    BoxShadow(
    color: Colors.white,
    offset: const Offset(0.0, 0.0),
    blurRadius: 0.0,
    spreadRadius: 0.0,
    ), //BoxShadow
    ],
    ),
    child:SingleChildScrollView(child:
      Column(children:[
        SizedBox(height:  MediaQuery.of(context).size.height*0.04,),
        Text("Welcome to TicToe Game",style: TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 35,
            shadows: [
              Shadow(
                color: shadowcolor3,
                blurRadius: 3,
              ),
              Shadow(
                color:shadowcolor3,
                blurRadius: 6,
              ),
              Shadow(
                color: shadowcolor3,
                blurRadius: 9,
              ),
            ],
            fontFamily: 'MsMadi',
            color: Colors.white
        ),),Padding(padding:EdgeInsets.only(left: 10,right: 10,top: 10),
        child:
        Image.asset("assets/tictoe.png"),),
 SizedBox(
   height: MediaQuery.of(context).size.height*0.1,
 ),
        Padding(padding: EdgeInsets.only(left: 10,right: 10),child:
 TextField(
   decoration: InputDecoration(
     filled: true,
     fillColor: Colors.white,
     hintText: 'First Player',
     contentPadding:
     const EdgeInsets.only(left: 14.0, bottom: 8.0, top: 8.0),
     focusedBorder: OutlineInputBorder(
       borderSide: BorderSide(color: Colors.white),
       borderRadius: BorderRadius.circular(25.7),
     ),
     enabledBorder: UnderlineInputBorder(
       borderSide: BorderSide(color: Colors.white),
       borderRadius: BorderRadius.circular(25.7),
     ),
   ),
   cursorColor: Colors.white,
        controller:controller1,
       ),),
        SizedBox(height: 10,),
        Padding(padding: EdgeInsets.only(left: 10,right: 10),child:
        TextField(
          decoration: InputDecoration(
            filled: true,
            fillColor: Colors.white,
            hintText: 'Second Player',
            contentPadding:
            const EdgeInsets.only(left: 14.0, bottom: 8.0, top: 8.0),
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.white),
              borderRadius: BorderRadius.circular(25.7),
            ),
            enabledBorder: UnderlineInputBorder(
              borderSide: BorderSide(color: Colors.white),
              borderRadius: BorderRadius.circular(25.7),
            ),
          ),
          controller:controller2,
        ),),
          ElevatedButton(onPressed:(){
            setState((){
              audioPlayer.open(Audio("assets/start.wav"));
            });
            Navigator.pushReplacement(context, MaterialPageRoute(builder: (context)=>MyHomePage(a: controller1.text,b: controller2.text,)));},
            child: Text("Start"),)]))
      )])))));
  }
}

class player{
  static const none="";
  static const X="X";
  static const O="O";
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.a, required this.b,});
final String a;
final String b;
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  static final countmatrix = 3;
  static final double size = 92;
  String lastmove = player.none;
  late List<List<String>>matrix;
  bool isPlaying = false;
  bool show = false;
  bool user = true;
  bool won = false;
  int i = 0,
      j = 0;
  Color shadowcolor1 = Colors.red;
  Color shadowcolor2 = Colors.purpleAccent;
  final controller = ConfettiController();

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  void initState() {
    super.initState();
    audioPlayer.open(
        Audio('assets/win.mp3'), autoStart: false, showNotification: false);
    controller.addListener(() {
      setState(() {
        isPlaying = controller.state == ConfettiControllerState.playing;
      });
    });
    setemptyfields();
  }

  AssetsAudioPlayer audioPlayer = AssetsAudioPlayer();

  void setemptyfields() =>
      setState(() =>
      matrix = List.generate(countmatrix,
              (_) => List.generate(countmatrix, (_) => player.none)));

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: backgrounddcolor(),
        appBar: AppBar(
          actions: [ElevatedButton(onPressed: () {
            Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (context)=>Splash()));
          }, child: Text("Change Player"))
          ],
        ),

        body: Stack(alignment: Alignment.topCenter,
            children: [Visibility(visible: !show,
              child:
              Text(lastmove == player.X
                  ? "${widget.b} this is your move"
                  : "${widget.a} this is your move", style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 35,
                  shadows: [
                    Shadow(
                      color: user == true ? shadowcolor1 : shadowcolor2,
                      blurRadius: 3,
                    ),
                    Shadow(
                      color: user == true ? shadowcolor1 : shadowcolor2,
                      blurRadius: 6,
                    ),
                    Shadow(
                      color: user == true ? shadowcolor1 : shadowcolor2,
                      blurRadius: 9,
                    ),
                  ],
                  fontFamily: 'MsMadi',
                  color: Colors.white
              )),),
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: Utils.modelBuilder(matrix, (x, value) => buildRow(x)),
              ),
              ConfettiWidget(confettiController: controller,
                  shouldLoop: true,
                  emissionFrequency: 0.08,
                  gravity: 0.3,
                  blastDirection: pi / 2,
                  createParticlePath: (size) {
                    final path = Path();
                    path.addPolygon([
                      Offset(20, 5),
                      Offset(8, 39.6),
                      Offset(38, 15.6),
                      Offset(2, 15.6),
                      Offset(32, 39.6),
                    ], true);
                    return path;
                  }
              ),
              ConfettiWidget(confettiController: controller,
                  shouldLoop: true,
                  emissionFrequency: 0.08,
                  gravity: 0.3,
                  blastDirection: 0,
                  createParticlePath: (size) {
                    final path = Path();
                    path.addPolygon([
                      Offset(20, 5),
                      Offset(8, 39.6),
                      Offset(38, 15.6),
                      Offset(2, 15.6),
                      Offset(32, 39.6),
                    ], true);
                    return path;
                  }
              ),
              ConfettiWidget(confettiController: controller,
                  shouldLoop: true,
                  emissionFrequency: 0.08,
                  gravity: 0.3,
                  blastDirection: pi,
                  createParticlePath: (size) {
                    final path = Path();
                    path.addPolygon([
                      Offset(20, 5),
                      Offset(8, 39.6),
                      Offset(38, 15.6),
                      Offset(2, 15.6),
                      Offset(32, 39.6),
                    ], true);
                    return path;
                  }
              ), Visibility(visible: show,
                  child: Positioned(
                      bottom: 30,
                      child: Column(
                          children: [
                            ElevatedButton(onPressed: () {
                              setState(() {
                                setemptyfields();
                                show = !show;
                                won = !won;
                                controller.stop();
                              });
                            }, child: Text("Restart")),
                            Text(won == true
                                ? (user == true
                                ? "Congratulations ${widget.a}"
                                : "Congratulations ${widget.b}")
                                : "Undeclared Result", style: TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: 30,
                                shadows: [
                                  Shadow(
                                    color: user == true
                                        ? shadowcolor1
                                        : shadowcolor2,
                                    blurRadius: 3,
                                  ),
                                  Shadow(
                                    color: user == true
                                        ? shadowcolor1
                                        : shadowcolor2,
                                    blurRadius: 6,
                                  ),
                                  Shadow(
                                    color: user == true
                                        ? shadowcolor1
                                        : shadowcolor2,
                                    blurRadius: 9,
                                  ),
                                ],
                                fontFamily: 'MsMadi',
                                color: Colors.white
                            )),
                            Text(won == true
                                ? "You Won By ${(i - j).abs()} move"
                                : "", style: TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: 25,
                                shadows: [
                                  Shadow(
                                    color: user == true
                                        ? shadowcolor1
                                        : shadowcolor2,
                                    blurRadius: 3,
                                  ),
                                  Shadow(
                                    color: user == true
                                        ? shadowcolor1
                                        : shadowcolor2,
                                    blurRadius: 6,
                                  ),
                                  Shadow(
                                    color: user == true
                                        ? shadowcolor1
                                        : shadowcolor2,
                                    blurRadius: 9,
                                  ),
                                ],
                                fontFamily: 'MsMadi',
                                color: Colors.white
                            ))
                          ])
                  ))
            ])
    );
  }

  Color getfieldcolor(String value) {
    switch (value) {
      case player.O:
        return Colors.blueAccent;
      case player.X:
        return Colors.redAccent;
      default:
        return Colors.white;
    }
  }

  Color backgrounddcolor() {
    final thismove = lastmove == player.X ? player.O : player.X;
    return getfieldcolor(thismove).withAlpha(120);
  }

  Widget buildRow(int x) {
    final values = matrix[x];

    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: Utils.modelBuilder(values, (y, model) => buildField(x, y)),
    );
  }

  Widget buildField(int x, int y) {
    final value = matrix[x][y];
    final color = getfieldcolor(value);
    return Container(
        margin: EdgeInsets.all(4),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(20.0),
            topRight: Radius.circular(20.0),
            bottomLeft: Radius.circular(20.0),
            bottomRight: Radius.circular(20.0),
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.black,
              offset: const Offset(2.0,
                2.0,
              ),
              blurRadius: 6.0,
              spreadRadius: 0.5,
            ),
            BoxShadow(
              color: Colors.black,
              offset: const Offset(
                -2.0,
                -2.0,
              ),
              blurRadius: 6.0,
              spreadRadius: 0.5,
            ), //BoxShadow
            BoxShadow(
              color: Colors.white,
              offset: const Offset(0.0, 0.0),
              blurRadius: 0.0,
              spreadRadius: 0.0,
            ), //BoxShadow
          ],
        ),
        child:
        ElevatedButton(onPressed: () {
          if (won != true) {
            if (lastmove == player.X) {
              i++;
            } else {
              j++;
            }
            selectfield(value, x, y);
            setState(() {
              audioPlayer.open(Audio('assets/click.wav'));
            });
          }
        },


          child: Text(value, style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 30,
              shadows: [
                Shadow(
                  color: Colors.grey,
                  blurRadius: 3,
                ),
                Shadow(
                  color: Colors.grey,
                  blurRadius: 6,
                ),
                Shadow(
                  color: Colors.black,
                  blurRadius: 9,
                ),
              ],

              color: Colors.white
          )), style: ElevatedButton.styleFrom(
              minimumSize: Size(size, size),
              primary: color

          ),)
    );
  }

  void selectfield(String value, int x, int y) {
    if (value == player.none) {
      final newvalue = lastmove == player.X ? player.O : player.X;
      setState(() {
        lastmove = newvalue;
        matrix[x][y] = newvalue;
      });
      if (iswinner(x, y)) {
        show = !show;
        controller.play();
        setState(() {
          audioPlayer.open(Audio('assets/win.mp3'));
          audioPlayer.open(Audio('assets/win.mp3'));
        });
        user = lastmove == player.X ? true : false;
        won = !won;
      }
    } else if (isended()) {
      setState(() {
        show = !show;
      });
    }
  }

  bool isended() => matrix.every((value) => value != player.none);

  bool iswinner(int x, int y) {
    var col = 0,
        row = 0,
        diag = 0,
        rdiag = 0;
    final player = matrix[x][y];
    final n = countmatrix;

    for (int i = 0; i < n; i++) {
      if (matrix[x][i] == player) col++;
      if (matrix[i][y] == player) row++;
      if (matrix[i][i] == player) diag++;
      if (matrix[i][n - i - 1] == player) rdiag++;
    }

    return row == n || col == n || diag == n || rdiag == n;
  }
}
