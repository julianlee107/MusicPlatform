/**
 * Created by lijunlin on 3/15/18.
 */
$(document).ready(function(){

  var myPlaylist = new jPlayerPlaylist({
    jPlayer: "#jplayer_N",
    cssSelectorAncestor: "#jp_container_N"
  },
      [
    {
      title:"彩虹",
      artist:"周杰伦",
      mp3:"http://music.163.com/song/media/outer/url?id=185809.mp3",
      poster: "images/m0.jpg"
    },
      {
        title:"等你下课（with 杨瑞代）",
          artist:"周杰伦",
          mp3:"http://music.163.com/song/media/outer/url?id=531051217.mp3"

      },
      {

      }

  ],

      {
    playlistOptions: {
      enableRemoveControls: true,
      autoPlay: false
    },
    swfPath: "static/js/jPlayer",
    supplied: "webmv, ogv, m4v, oga, mp3",
    smoothPlayBar: true,
    keyEnabled: true,
    audioFullScreen: false
  });

  $(document).on($.jPlayer.event.pause, myPlaylist.cssSelector.jPlayer,  function(){
    $('.musicbar').removeClass('animate');
    $(".jp-play-me").removeClass('active');
    $('.jp-play-me').parent('li').removeClass('active');
  });

  $(document).on($.jPlayer.event.play, myPlaylist.cssSelector.jPlayer,  function(){
    $('.musicbar').addClass('animate');
  });

  $(document).on('click', '.jp-play-me', function(e){
    e && e.preventDefault();
    var $this = $(e.target);
    if (!$this.is('a')) $this = $this.closest('a');

    $('.jp-play-me').not($this).removeClass('active');
    $('.jp-play-me').parent('li').not($this.parent('li')).removeClass('active');

    $this.toggleClass('active');
    $this.parent('li').toggleClass('active');
    if( !$this.hasClass('active') ){
      myPlaylist.pause();
    }else{
      var i = Math.floor(Math.random() * (1 + 7 - 1));
      myPlaylist.play(i);
    }

  })

  });
