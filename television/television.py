class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the Television with default settings."""
        self.status: bool = False
        self.channel: int = self.MIN_CHANNEL
        self.volume: int = self.MIN_VOLUME
        self.muted: bool = False

    def power(self) -> None:
        """Toggle the power status of the TV."""
        self.status = not self.status

    def mute(self) -> None:
        """Mute or unmute the TV if it is powered on."""
        if self.status:
            self.muted = not self.muted

    def channel_up(self) -> None:
        """Increase the channel value or loop back to MIN_CHANNEL."""
        if self.status:
            self.channel = (
                self.channel + 1
                if self.channel < self.MAX_CHANNEL
                else self.MIN_CHANNEL
            )

    def channel_down(self) -> None:
        """Decrease the channel value or loop back to MAX_CHANNEL."""
        if self.status:
            self.channel = (
                self.channel - 1
                if self.channel > self.MIN_CHANNEL
                else self.MAX_CHANNEL
            )

    def volume_up(self) -> None:
        """Increase the volume if it is below MAX_VOLUME and not muted."""
        if self.status and not self.muted:
            self.volume = min(self.volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease the volume if it is above MIN_VOLUME and not muted."""
        if self.status and not self.muted:
            self.volume = max(self.volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """Return a string representation of the Television's state."""
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume if not self.muted else 0}"
