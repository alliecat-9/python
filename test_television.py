import pytest
from television import Television


def test_init():
    tv = Television()
    assert not tv.status
    assert tv.channel == Television.MIN_CHANNEL
    assert tv.volume == Television.MIN_VOLUME
    assert not tv.muted


def test_power():
    tv = Television()
    tv.power()
    assert tv.status
    tv.power()
    assert not tv.status


def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv.muted
    tv.mute()
    assert not tv.muted


def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL + 1
    tv.channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL


def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL
    tv.channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL


def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME + 1
    tv.volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME


def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()  # Increase volume first
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME
