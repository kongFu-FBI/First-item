class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 5
        self.ship_limit = 3

        # 子弹设置 宽3像素 高15像素 深灰色子弹
        self.bullet_speed = 2.0
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 300  # 设置屏幕上出现子弹的最大数

        self.alien_speed = 9.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
